"""This package generates labels/ calculates the number of each label of images through "EncodedPixels" attribute."""
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt  # plt - Graphs Plot Library


def label_gen(encoded_pixels):

    """Define a function that generates the label indicating ships"""

    has_ship = ()
    for img in tqdm(encoded_pixels, unit=' items', desc='Labeling CSV file'):
        if pd.isna(img):
            has_ship = has_ship + ('0',)
        else:
            has_ship = has_ship + ('1',)
    return has_ship


def label_num_calc(serial):

    """Define a function that calculates the number of each label"""

    has_ship = 0
    no_ship = 0
    for n in serial:
        if n == '1':
            has_ship += 1
        else:
            no_ship += 1
    data = [has_ship, no_ship]
    return data


def label_stat_bar(input_tuple, save_dir):

    """This function visualizes the statistical data of labels by plotting a bar chart."""

    # Generate figure
    plt.figure(0)
    # Add a title
    plt.suptitle(t="Statistics of Raw Data")
    # Generate left side bar
    plt.bar(x=0, height=input_tuple[0], width=50, color='YellowGreen', bottom=0, align='center',
            tick_label="HAVE SHIPS")
    # Adding text to left side bar
    plt.text(x=0, y=input_tuple[0], horizontalalignment='center', s=input_tuple[0])
    # Generate right side bar
    plt.bar(x=100, height=input_tuple[1], width=50, color='IndianRed', bottom=0, align='center',
            tick_label="DON'T HAVE SHIPS")
    # Adding text to right side bar
    plt.text(x=100, y=input_tuple[1], horizontalalignment='center', s=input_tuple[1])
    # Adding label to x-axis
    plt.xlabel("Status", color='b')
    # Adding label to y-axis
    plt.ylabel("Number of images", color='b')
    plt.savefig(save_dir + "Statistics.png")
    plt.show()
