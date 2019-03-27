import os
# Calculating time consuming
import time
import pandas as pd

from skimage import io
from PIL import Image


class csv_open:
    def __enter__(self):
        return pd.read_csv(DATASET_DIR + DATASET_CSV)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("type:", exc_type)
        print("value:", exc_val)
        print("trace:", exc_tb)


def get_csv_file():
    return csv_open()


df_attribute = ["ImageId",
                "EncodedPixels",
                "Shape",
                "Width",
                "Height",
                "#Channel",
                "#Pixel",
                "MaxPixel",
                "MinPixel",
                "AveragePixel",
                "Directory"
                ]


# Define function for data analysis

def image_analyser(input_df):
    input_df['Directory'] = DATASET_DIR + DATASET_FOLDER + input_df['ImageId']
    output_df = pd.DataFrame(data=None, columns=df_attribute)
    new_index = 0
    counter = 0
    last_milestone = 0
    for index, row in input_df.iterrows():
        if os.path.exists(row['Directory']):
            stat = io.imread(row['Directory'])  # Open the image and convert into numpy ndarray
            output_df.loc[new_index, 'ImageId'] = row['ImageId']
            output_df.loc[new_index, 'EncodedPixels'] = row['EncodedPixels']
            output_df.loc[new_index, 'Shape'] = stat.shape  # Shape
            output_df.loc[new_index, 'Width'] = stat.shape[0]  # Width
            output_df.loc[new_index, 'Height'] = stat.shape[1]  # Height
            output_df.loc[new_index, '#Channel'] = stat.shape[2]  # Number of channels
            output_df.loc[new_index, '#Pixel'] = stat.size  # Number of pixels
            output_df.loc[new_index, 'MaxPixel'] = stat.max()  # Maximum pixel value
            output_df.loc[new_index, 'MinPixel'] = stat.min()  # Minimum pixel value
            output_df.loc[new_index, 'AveragePixel'] = stat.mean  # Average pixel value
            output_df.loc[new_index, 'Directory'] = row['Directory']

            # Memory saving
            input_df.drop(index=index)
            del stat

        else:
            print("\"" + row['ImageId'] + "\"" + " does not exist.")
            counter += 1

        new_index += 1

        if new_index//1000 > last_milestone:
            last_milestone = new_index//1000
            print("Milestone of 1000 images: ", last_milestone)

    print(counter, " images are not founded according to csv.")
    return output_df

# Start of main section


# FOR TEST USAGE
DATASET_FOLDER = "train_v2\\"
DATASET_DIR = "E:\\Developing\\TrainingSet\\"
DATASET_CSV = "train_ship_segmentations_v2.csv"

# Start time indicator
start_time_formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
start_time = time.process_time()

# Read csv and convert into data frame
with get_csv_file() as csv_file:
    training_df = csv_file
    print("File open success!")

result_df = image_analyser(training_df)
result_df.to_csv(DATASET_DIR + "Result.csv")

# End time indicator
end_time = time.process_time()
end_time_formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
time_length = end_time - start_time

print("Started at:" + start_time_formatted + ".\n")
print("Finished at:" + start_time_formatted + ".\n")
print("Cost time:" + str(time_length) + " seconds.")

