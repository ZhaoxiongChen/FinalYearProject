# pandas - Data Science Utilities
import pandas as pd
# tqdm - Progress Bar for Python
from tqdm import tqdm
# plt - Graphs Plot Library
import matplotlib.pyplot as plt
# os Libraries
import os
import shutil
# Keras Pre-processing libraries
from keras.preprocessing.image import ImageDataGenerator
# train_test_split - Splitting Training Set
from sklearn.model_selection import train_test_split

'''Section of labeling images'''


# Define a function that generates the label indicating ships
def label_gen(encoded_pixels):
    has_ship = ()
    for img in tqdm(encoded_pixels, unit=' items', desc='Labeling CSV file'):
        if pd.isna(img):
            has_ship = has_ship + ('0',)
        else:
            has_ship = has_ship + ('1',)
    return has_ship


# Define a function that calculates the number of each label
def calculate_label(input):
    has_ship = 0
    no_ship = 0
    for n in input:
        if n == '1':
            has_ship += 1
        else:
            no_ship += 1
    data = [has_ship, no_ship]
    return data


# Define a function that visualizes the statistical data of labels
def bar_chart(input, labels, title):
    # Generate figure
    plt.figure(0)
    # Add a title
    plt.suptitle(t=title)
    # Generate left side bar
    plt.bar(x=0, height=input[0], width=50, color='YellowGreen', bottom=0, align='center', tick_label=labels[0][0])
    # Adding text to left side bar
    plt.text(x=0, y=input[0], horizontalalignment='center', s=input[0])
    # Generate right side bar
    plt.bar(x=100, height=input[1], width=50, color='IndianRed', bottom=0, align='center', tick_label=labels[0][1])
    # Adding text to right side bar
    plt.text(x=100, y=input[1], horizontalalignment='center', s=input[1])
    # Adding label to x-axis
    plt.xlabel("Status", color='b')
    # Adding label to y-axis
    plt.ylabel(labels[1], color='b')
    plt.show()


SAMPLE_SIZE = 100
TEST_RATIO = 0.2
BATCH_SIZE = 2
DATASET_DIR = "E:\\Developing\\TrainingSet\\"
DATASET_CSV = "train_ship_segmentations_v2.csv"


class csv_open:
    def __enter__(self):
        return pd.read_csv(DATASET_DIR + DATASET_CSV)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("type:", exc_type)
        print("value:", exc_val)
        print("trace:", exc_tb)


def get_csv_file():
    return csv_open()


# Read csv file using pandas
with get_csv_file() as csv_file:
    items = csv_file
    print("File open success!")

# Add a column to dataframe to store the directory of each image
items['Directory'] = DATASET_DIR + "train_v2\\" + items['ImageId']

# Randomly sample SAMPLE_SIZE images
items = items.sample(n=SAMPLE_SIZE)

# Append labels for DataFrame items
items['HasShip'] = label_gen(items['EncodedPixels'].values)

# Visualize results
bar_chart(input=calculate_label(items['HasShip'].values),
          labels=[["HAVE SHIPS", "DON'T HAVE SHIPS"], "Number of images"],
          title="Statistics of Sample")

'''Section of image pre-processing'''


# Image pre-processing
def image_augmentation(generator_config, input_dataframe, mode, batch_size):
    prep_result = generator_config.flow_from_dataframe(
        dataframe=input_dataframe,
        directory=os.path.dirname(input_dataframe['Directory'].values[0]),
        x_col='Directory',
        y_col='HasShip',
        target_size=(256, 256),
        color_mode='rgb',
        class_mode='sparse',
        batch_size=batch_size,
        shuffle=True
    )
    iter_num = int(len(input_dataframe)/batch_size)
    for i in tqdm(range(iter_num), unit=' batches', desc='Pre-processing images'):
        prep_result.next()
    return prep_result


# Output augmented sample
def output_aug_images(train_generator, test_generator, input_dataframe):
    save_dir = DATASET_DIR + 'augmentation_sample'
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    op1 = train_generator.flow_from_dataframe(
        dataframe=input_dataframe,
        directory=os.path.dirname(input_dataframe['Directory'].values[0]),
        x_col='Directory',
        y_col='HasShip',
        target_size=(256, 256),
        color_mode='rgb',
        class_mode='sparse',
        shuffle=False,
        batch_size=1,
        save_to_dir=save_dir,
        save_prefix='train_config_',
        save_format='jpg'
    )
    op1.next()
    op2 = test_generator.flow_from_dataframe(
        dataframe=input_dataframe,
        directory=os.path.dirname(input_dataframe['Directory'].values[0]),
        x_col='Directory',
        y_col='HasShip',
        target_size=(256, 256),
        color_mode='rgb',
        class_mode='sparse',
        shuffle=False,
        batch_size=1,
        save_to_dir=save_dir,
        save_prefix='test_config_',
        save_format='jpg'
    )
    op2.next()
    shutil.copy(src=input_dataframe['Directory'].values[0], dst=save_dir)


# Spilt up images
train, test = train_test_split(items, test_size=TEST_RATIO)

# Set up pre-processing configurations respectively
prep_train_generator = ImageDataGenerator(rescale=1./225, zoom_range=0.2, horizontal_flip=True, shear_range=0.2)
prep_test_generator = ImageDataGenerator(rescale=1./225)

# Execute image augmentation
prep_train = image_augmentation(prep_train_generator, train, 'train', BATCH_SIZE)
prep_test = image_augmentation(prep_test_generator, test, 'test', BATCH_SIZE)

# Visualizing image augmentation effect
sample = pd.read_csv(DATASET_DIR + 'Sample.csv')
sample['Directory'] = DATASET_DIR + sample['ImageId']
sample['HasShip'] = label_gen(sample['EncodedPixels'].values)
output_aug_images(prep_train_generator, prep_test_generator, sample)

# END OF DataPrep.py
