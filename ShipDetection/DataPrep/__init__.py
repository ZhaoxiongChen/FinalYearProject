from sklearn.model_selection import train_test_split  # train_test_split - Splitting Training Set
import pandas as pd  # pandas - Data Science Utilities

import SelectionValidation as sv
import CSVUtil as csvUtil
import DataPrep.LabelUtil as labelUtil
import DataPrep.MethodDemo as md
import DataPrep.AugConfig as config

# Hyper parameters
SAMPLE_SIZE = 25000
TEST_RATIO = 0.2
BATCH_SIZE = 2
DATASET_DIR = "E:\\Developing\\TrainingSet\\"
DATASET_CSV = "TrainingSetAnalysis.csv"

# CLI messages
SCALE_MENU = "\nAvailable scale of dataset:\nA  Sampled 50k images.\nB  Whole DataSet"
SCALE_DICT = {"A": "Sampled_50k", "B": "WholeDataSet"}
MODEL_MENU = "\nAvailable model to train:\nCNNProto\nResNet50\nVGG16\nVGG19"
MODEL_DICT = {"CNNProto": 256, "ResNet50": 224, "VGG16": 224, "VGG19": 224}
WELCOME_MESG = "Please select or input:"

# Read csv file using pandas
with csvUtil.get_dataframe(DATASET_DIR, DATASET_CSV) as csv_file:
    print("File opening...")
    raw_data = csv_file
    print("File open success!")
# CLI menus
input_validation = sv.SelectionValidation(selection_dict=SCALE_DICT,
                                          menu_message=SCALE_MENU,
                                          welcome_message=WELCOME_MESG)
scale_select = input_validation.validation()

input_validation = sv.SelectionValidation(selection_dict=MODEL_DICT,
                                          menu_message=MODEL_MENU,
                                          welcome_message=WELCOME_MESG)
model_select = input_validation.validation()

# Mode confirm
print("Mode " + SCALE_DICT[scale_select] + " have been selected.\n")

if scale_select == "A":
    print("Since 25,000 original images will be used, data augmentation will be turned ON.")
    # Sample SAMPLE_SIZE images
    raw_data = raw_data.sample(n=SAMPLE_SIZE, replace=False, weights=None, random_state=1)

else:
    print("Since all of the images will be used, data augmentation will be turned OFF.")

# Append labels for DataFrame items
raw_data['HasShip'] = labelUtil.label_gen(raw_data['EncodedPixels'].values)
# Visualize results
labelUtil.label_stat_bar(input_tuple=labelUtil.label_num_calc(raw_data['HasShip'].values),
                         save_dir=DATASET_DIR)
# Spilt up images
train_data, test_data = train_test_split(raw_data, random_state=1, test_size=TEST_RATIO)

# Visualizing image augmentation effect
sample_df = pd.read_csv(DATASET_DIR + 'Sample.csv')
sample_df['Directory'] = DATASET_DIR + sample_df['ImageId']
sample_df['HasShip'] = labelUtil.label_gen(sample_df['EncodedPixels'].values)

if scale_select == "A":
    selected_config = config.sample_train_config
else:
    selected_config = config.preprocess_config

# DataFrameIterator: Generates unlimited number of images according to the configuration
# A.k.a Source of the pre-processed images
prep_train = config.prep_exec(config=selected_config,
                              input_df=train_data,
                              batch_size=BATCH_SIZE,
                              side_length=MODEL_DICT[model_select])
prep_test = config.prep_exec(config=selected_config,
                             input_df=test_data,
                             batch_size=BATCH_SIZE,
                             side_length=MODEL_DICT[model_select])
sample = md.MethodDemo(train_config=config.sample_train_config,
                       test_config=config.preprocess_config,
                       input_df=sample_df,
                       side_length=MODEL_DICT[model_select],
                       save_dir=DATASET_DIR + "Sample")
sample.output_aug_sample()
