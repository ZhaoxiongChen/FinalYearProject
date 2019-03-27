import matplotlib.pyplot as plt
import time



path = 'results'
name = 'adam'
DATE = time.strftime("%Y-%m-%d_%H%M", time.localtime())
MODEL = input("Please input the directory of the trained model:")

plt.plot(init.fitted_model.history['acc'])
plt.plot(init.fitted_model.history['val_acc'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper left')

plt.show()
plt.savefig(DATE + "Accuracy")

plt.figure()
plt.gcf().clear()
plt.plot(init.fitted_model.history['loss'])
plt.plot(init.fitted_model.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper left')

plt.show()
plt.savefig(DATE + "Loss")
