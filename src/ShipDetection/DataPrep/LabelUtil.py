"""This package generates labels/ calculates the number of each label of images through "EncodedPixels" attribute."""
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt


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


def label_stat_bar(input_tuple, save_dir, title, color_dict):

    """This function visualizes the statistical data of labels by plotting a bar chart."""

    # Resolution: 800*600@300dpi
    plt.rcParams['figure.figsize'] = (8, 6)
    plt.figure(dpi=300)
    # Generate figure
    plt.figure(0)
    # Add a title
    plt.title(title, fontsize=16)
    # Define tick label list
    LABEL_LIST = ['True', 'False']
    # Generate left side bar
    # Name of color see:https://xkcd.com/color/rgb/
    # 954 most common RGB monitor colors
    # TRUE: Sampled_50k: YellowGreen/Whole DataSet: RoyalBlue
    plt.bar(x=0, height=input_tuple[0], width=50, color=color_dict["True"], bottom=0, align='center')
    # Adding text to left side bar
    plt.text(x=0, y=input_tuple[0], horizontalalignment='center', s=input_tuple[0], fontsize=16)
    # Generate right side bar
    # FALSE: Sampled_50k: IndianRed/Whole DataSet: Orange
    plt.bar(x=100, height=input_tuple[1], width=50, color=color_dict["False"], bottom=0, align='center')
    # Adding text to right side bar
    plt.text(x=100, y=input_tuple[1], horizontalalignment='center', s=input_tuple[1], fontsize=16)
    # Adding label to x-axis
    plt.xlabel("Ship Existence", fontsize=16)
    # Adding label to y-axis
    plt.ylabel("Number of images", fontsize=16)
    plt.xticks(ticks=[0, 100], labels=LABEL_LIST)
    plt.savefig(fname=save_dir + title +".png")
    plt.show()
