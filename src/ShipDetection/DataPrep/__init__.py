from sklearn.model_selection import train_test_split
import pandas as pd
from Utilities import SelectionValidation as sv
from Utilities import CSVOpen
import DataPrep.LabelUtil as lu
import DataPrep.MethodDemo as md
import DataPrep.AugConfig as config
import GlobalVariable as gv

# Hyper parameters
SAMPLE_SIZE = 25000
TEST_RATIO = 0.2
# BATCH_SIZE = 100
BATCH_SIZE = 250
# BATCH_SIZE = 1000 - OOM
# BATCH_SIZE = 2 - TOO SLOW/OVER-FITTED

print("Batch size = " + str(BATCH_SIZE))

dataset_dir = gv.project_dir.dataset_dir
dataset_csv = gv.project_dir.csv_label

# Read csv file using pandas
with CSVOpen.get_dataframe(dataset_dir, dataset_csv) as csv_file:
    print("File opening...")
    raw_data = csv_file
    print("File open success!")

# CLI messages
SCALE_MENU = "\nAvailable scale of dataset:\nA  Sampled 25k images.\nB  Whole DataSet"
SCALE_DICT = {"A": "Sampled", "B": "Whole DataSet"}

# CLI menus
input_validation = sv.SelectionValidation(selection_dict=SCALE_DICT,
                                          menu_message=SCALE_MENU,
                                          welcome_message="Please select a mode:")
scale_select = input_validation.validation()

# Mode confirm
print("Mode " + SCALE_DICT[scale_select] + " have been selected.\n")

color_dict = {}

if scale_select == "A":
    print("Sampled mode will use 25,000 original images, data augmentation will be turned ON.")
    raw_data = raw_data.sample(n=SAMPLE_SIZE, replace=False, weights=None, random_state=1)
    # Sampled_50k: True: YellowGreen/False: IndianRed
    color_dict = {"True": "YellowGreen", "False": "IndianRed"}
else:
    print("Since all of the images will be used, data augmentation will be turned OFF.")
    # Whole DataSet: True: RoyalBlue/False: Orange
    color_dict = {"True": "RoyalBlue", "False": "Orange"}

# Append labels for DataFrame items
raw_data['HasShip'] = lu.label_gen(raw_data['EncodedPixels'].values)
# Visualize results
lu.label_stat_bar(input_tuple=lu.label_num_calc(raw_data['HasShip'].values),
                  save_dir=dataset_dir,
                  title="Statistics of Appointed Dataset Scope",
                  color_dict=color_dict)
# Drop raw data columns
raw_data = raw_data.drop(columns=['EncodedPixels',
                                  'Width',
                                  'Height',
                                  '#Channel',
                                  '#Pixel',
                                  'MaxPixel',
                                  'MinPixel',
                                  'AveragePixel'])

# Spilt up images
train_data, test_data = train_test_split(raw_data, random_state=1, test_size=TEST_RATIO)

lu.label_stat_bar(input_tuple=lu.label_num_calc(train_data['HasShip'].values),
                  save_dir=dataset_dir,
                  title="Statistics of Actual Training Set Data",
                  color_dict=color_dict)
lu.label_stat_bar(input_tuple=lu.label_num_calc(test_data['HasShip'].values),
                  save_dir=dataset_dir,
                  title="Statistics of Actual Test Set Data",
                  color_dict=color_dict)

# Visualizing image augmentation effect
sample_df = pd.read_csv(dataset_dir + 'Sample.csv')
sample_df['Directory'] = dataset_dir + sample_df['ImageId']
sample_df['HasShip'] = lu.label_gen(sample_df['EncodedPixels'].values)

if scale_select == "A":
    selected_config = config.augmentation_config
else:
    selected_config = config.preprocess_config

# DataFrameIterator: Generates unlimited number of images according to the configuration
# A.k.a Source of the pre-processed images
prep_train = config.prep_exec(config=selected_config,
                              input_df=train_data,
                              batch_size=BATCH_SIZE,
                              side_length=256)
prep_test = config.prep_exec(config=selected_config,
                             input_df=test_data,
                             batch_size=BATCH_SIZE,
                             side_length=256)
sample = md.MethodDemo(train_config=selected_config,
                       test_config=config.preprocess_config,
                       input_df=sample_df,
                       side_length=256,
                       save_dir=dataset_dir)
sample.output_aug_sample()
