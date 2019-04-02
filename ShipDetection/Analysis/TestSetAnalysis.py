from skimage import io
import csv
import os
import time

# For avoiding bug of truncated image (occurred in 2019-1-9)
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


csv_head = ["FileName", "Shape", "Width", "Height", "#Channel", "#Pixel", "MaxPixel", "MinPixel", "AveragePixel",
            "Type", "Extension", "Size"]


def create_csv(name, path):

    """This function is used for creating .csv file"""

    path = path + "\\" + name + ".csv"
    with open(path, 'w', newline='') as file:
        csv_write = csv.writer(file)
        csv_write.writerow(csv_head)
    return path


def log_csv(path, data_row):

    """This function is used for writing .csv file"""

    with open(path, 'a+', newline='') as file:
        csv_write = csv.writer(file)
        csv_write.writerow(data_row)


def analyser(csv_path, file_dir):

    """This function is used for data analysis"""

    for root, dirs, files in os.walk(file_dir):
        for item in files:
            img = io.imread(file_dir + "\\" + item)  # Open image in skimage
            img_attr = []
            img_attr.append(item)
            img_attr.append(img.shape)  # Shape
            img_attr.append(img.shape[0])  # Width
            img_attr.append(img.shape[1])  # Height
            img_attr.append(img.shape[2])  # Number of channels
            img_attr.append(img.size)  # Number of pixels
            img_attr.append(img.max())  # Maximum pixel value
            img_attr.append(img.min())  # Minimum pixel value
            img_attr.append(img.mean())  # Average pixel value
            img_attr.append(img.dtype.name)  # Type to store image
            img_attr.append(os.path.splitext(item)[1])
            img_attr.append(os.path.getsize(file_dir + "\\" + item))  # Size of image
            log_csv(csv_path, img_attr)  # Write to csv file


# Start of main section

# FOR TEST USAGE
DATASET_FOLDER = "test_v2\\"
DATASET_DIR = "E:\\Developing\\TrainingSet\\"

test_csv = create_csv("TestSetAnalysis", DATASET_DIR)

# Start time
t0_formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
t0 = time.process_time()

analyser(test_csv, DATASET_DIR + DATASET_FOLDER)

# End time
t1 = time.process_time()
t1_formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
time_length = t1 - t0

# Time result
print("Started at:" + t0_formatted + ".\n")
print("Finished at:" + t1_formatted + ".\n")
print("Cost time:" + str(time_length) + " seconds.")
