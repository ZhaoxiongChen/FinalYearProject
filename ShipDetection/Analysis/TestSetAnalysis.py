from skimage import io
import csv
import os
import time


# Define function for creating .csv file
def create_csv(name, path):
    path = path + "\\" + name + ".csv"
    with open(path, 'w', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ["FileName", "Shape",
                    "Width", "Height", "#Channel",
                    "#Pixel", "MaxPixel", "MinPixel", "AveragePixel",
                    "Type", "Extension", "Size"]
        csv_write.writerow(csv_head)
    return path


# Define function for logging .csv file
def log_csv(path, data_row):
    with open(path, 'a+', newline='') as file:
        csv_write = csv.writer(file)
        csv_write.writerow(data_row)


# Define function for data analysis
def analyser(csv_path, file_dir):
    start_time_formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    start_time = time.process_time()

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

    end_time = time.process_time()
    end_time_formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    time_length = end_time - start_time
    exec_sum_header = ["Started at", "Finished at", "Executed time"]
    exec_sum_data = [start_time_formatted, end_time_formatted, time_length]
    log_csv(csv_path, exec_sum_header)
    log_csv(csv_path, exec_sum_data)


# Start of main section

# FOR TEST USAGE
DATASET_FOLDER = "test_v2\\"
DATASET_DIR = "E:\\Developing\\TrainingSet\\"

test_csv = create_csv("test_set_analysis", DATASET_DIR)
analyser(test_csv, DATASET_DIR + DATASET_FOLDER)
