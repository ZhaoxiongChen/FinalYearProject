import matplotlib.pyplot as plt


class FittedModel:
    """This class provides method to analyse the trained model."""

    def __init__(self, input_model, date, save_dir):
        self.input_model = input_model
        self.date = date
        self.save_dir = save_dir

    def save_acc_fig(self):

        """This function generates figure of accuracy."""
        plt.figure()
        plt.gcf().clear()
        plt.plot(self.input_model.fitted_model.history['acc'])
        plt.plot(self.input_model.fitted_model.history['val_acc'])
        plt.title('Model Accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()
        plt.savefig(self.save_dir + self.date + "_Accuracy.png")

    def save_loss_fig(self):

        """This function generates figure of loss."""

        plt.figure()
        plt.gcf().clear()
        plt.plot(self.input_model.fitted_model.history['loss'])
        plt.plot(self.input_model.fitted_model.history['val_loss'])
        plt.title('Model Loss')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()
        plt.savefig(self.save_dir + self.date + "_Loss.png")

    def f2_evaluation(self):
        print("TO BE UPDATED")

    def predict_image(self, test_image_dir):
        self.input_model.predict()

