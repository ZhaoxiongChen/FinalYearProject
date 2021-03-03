import os
import csv
import GlobalVariable as gv
from skimage import io
from Utilities import CSVOpen as csv_util
from Utilities import TimeStamp as ts

# For avoiding bug of truncated image (occurred in 2019-1-9)
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

df_attribute = ["ImageId", "EncodedPixels", "Width", "Height", "#Channel", "#Pixel", "MaxPixel", "MinPixel",
                "AveragePixel", "Directory"]


def create_csv(path, name):
    path = path + "\\" + name + ".csv"
    with open(path, 'w', newline='') as file:
        csv_write = csv.writer(file)
        csv_write.writerow(df_attribute)
    return path


# Define function for data analysis
def image_analyser(input_df, input_csv_path):
    input_df['Directory'] = dataset_folder + input_df['ImageId']
    new_index = 0
    counter = 0
    last_milestone = 0

    # Open csv file
    with open(input_csv_path, 'a+', newline='') as file:
        output_csv = csv.writer(file)

        # Iteration through dataframe rows
        for index, row in input_df.iterrows():
            if os.path.exists(row['Directory']):
                try:
                    img = io.imread(row['Directory'])  # Open the image and convert into numpy ndarray
                    img_attr = []
                    img_attr.append(row['ImageId'])
                    img_attr.append(row['EncodedPixels'])
                    img_attr.append(img.shape[0])  # Width
                    img_attr.append(img.shape[1])  # Height
                    img_attr.append(img.shape[2])  # Number of channels
                    img_attr.append(img.size)  # Number of pixels
                    img_attr.append(img.max())  # Maximum pixel value
                    img_attr.append(img.min())  # Minimum pixel value
                    img_attr.append(img.mean())  # Average pixel value
                    img_attr.append(row['Directory'])
                    output_csv.writerow(img_attr)
                except(OSError, NameError):
                    print("OSError: truncated images:" + row['ImageId'])

                # Memory saving
                input_df.drop(index=index)

            else:
                print("\"" + row['ImageId'] + "\"" + " does not exist.")
                counter += 1

            new_index += 1

            if new_index//BATCH_SIZE > last_milestone:
                last_milestone = new_index//BATCH_SIZE
                print("Milestone of", BATCH_SIZE, "images: ", last_milestone)

    print(counter, " images are not founded according to csv.")


# Start of main section
BATCH_SIZE = 1000
dataset_folder = gv.project_dir.train_dir
dataset_dir = gv.project_dir.dataset_dir
dataset_csv = "train_ship_segmentations_v2.csv"

# Time start
time_stamp = ts.TimeStamp()
time_stamp.start()

# Operation: Read csv and convert into data frame
with csv_util.get_dataframe(dataset_dir, dataset_csv) as csv_file:
    training_df = csv_file
    print("File open success!")

file_name = "TrainingSetAnalysis"

processed_csv = create_csv(dataset_dir, file_name)
image_analyser(training_df, processed_csv)

# Time finish
time_stamp.stop()

# Time summary
time_stamp.summary()
del time_stamp
