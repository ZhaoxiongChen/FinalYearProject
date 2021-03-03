import matplotlib.pyplot as plt
import keras
import os
import numpy as np
from keras.preprocessing import image
from keras.utils.vis_utils import plot_model


class FittedModel:
    """This class provides method to analyse the trained model."""

    def __init__(self, model_dir, model_prefix, save_dir):

        self.model_prefix = model_prefix
        self.model_arch_name = model_prefix.split("_", 1)[1]
        self.model_name = model_dir + "\\" + model_prefix
        self.input_model = keras.models.load_model(self.model_name + "_trained_model.h5")

        # Open history text
        with open(self.model_name + "_history.txt", "r") as model_history:
            # Convert to dictionary
            self.input_history = eval(model_history.read())
            print("Successfully opened history.")

        self.save_dir = save_dir + "\\"

    def save_acc_fig(self):
        """This function generates figure of accuracy."""

        # Resolution: 1024*768@300dpi
        plt.rcParams['figure.figsize'] = (10.24, 7.68)
        plt.figure(dpi=300)
        plt.gcf().clear()
        plt.plot(self.input_history['acc'], marker='x')
        plt.plot(self.input_history['val_acc'], marker='.')
        plt.title('Model Accuracy of ' + self.model_arch_name, fontsize=20)
        plt.ylabel('Accuracy', fontsize=20)
        plt.xlabel('Epoch', fontsize=20)
        plt.xticks(ticks=list(range(0, 20, 1)), labels=list(range(1, 21, 1)))
        plt.legend(['TRAIN', 'TEST'], loc='upper left')

        for x, ytr, yte in zip(range(0, 20, 1), self.input_history['acc'], self.input_history['val_acc']):
            plt.text(x=x, y=ytr, s=float('%.4f' % ytr), ha='center', va='bottom', fontsize=8)
            plt.text(x=x, y=yte, s=float('%.4f' % yte), ha='center', va='bottom', fontsize=8)

        plt.savefig(fname=self.save_dir + self.model_prefix + "_Accuracy.png")
        plt.show()

    def save_loss_fig(self):
        """This function generates figure of loss."""

        # Resolution: 1024*768@300dpi
        plt.rcParams['figure.figsize'] = (10.24, 7.68)
        plt.figure(dpi=300)
        plt.gcf().clear()
        plt.plot(self.input_history['loss'], marker='x')
        plt.plot(self.input_history['val_loss'], marker='.')
        plt.title('Model Loss of ' + self.model_arch_name, fontsize=20)
        plt.ylabel('Loss', fontsize=20)
        plt.xlabel('Epoch', fontsize=20)
        plt.xticks(ticks=list(range(0, 20, 1)), labels=list(range(1, 21, 1)))
        plt.legend(['TRAIN', 'TEST'], loc='upper left')

        for x, ytr, yte in zip(range(0, 20, 1), self.input_history['loss'], self.input_history['val_loss']):
            plt.text(x=x, y=ytr, s=float('%.4f' % ytr), ha='center', va='bottom', fontsize=8)
            plt.text(x=x, y=yte, s=float('%.4f' % yte), ha='center', va='bottom', fontsize=8)

        plt.savefig(fname=self.save_dir + self.model_prefix + "_Loss.png")
        plt.show()

    def save_arch_fig(self):
        plot_model(self.input_model, to_file=self.save_dir + self.model_prefix + '_Summary.svg',
                   show_shapes=True, show_layer_names=True)

    def predict_image(self):

        test_image_dir = input("Please input image directory to predict:")
        images = []
        for root, dirs, files in os.walk(test_image_dir):
            images = files
        images_array = np.empty(shape=[0, 256, 256, 3])
        for items in images:
            img = image.load_img(test_image_dir + "\\" + items, target_size=(256, 256))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            images_array = np.concatenate((images_array, x), axis=0)

        result = self.input_model.predict(x=images_array, verbose=0)

        predict_font = {"color": "white", "size": "16"}

        i = 0
        while i < len(images):
            print("Possibility of ship existence in \"" + images[i] + "\" is: " + str(result[i][0]))
            # Resolution: 500*500@300dpi
            plt.rcParams['figure.figsize'] = (5, 5)
            plt.figure(dpi=300)
            plt.gcf().clear()
            plt.imshow(image.load_img(test_image_dir + "\\" + images[i], target_size=(256, 256)))
            plt.axis('on')
            plt.title("Prediction result of " + images[i] + "\nModel: " + self.model_prefix)
            plt.text(x=0, y=0, s="Ship existence possibility:\n" + str(result[i][0]), va="top", fontdict=predict_font)
            plt.savefig(fname=self.save_dir + self.model_prefix + "_Prediction_" + images[i].split(".")[0] + ".png")
            plt.show()
            i = i + 1
