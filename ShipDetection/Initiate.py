# import DataLoad module to analyse data
import time
time_data_prep_start = time.time()
print("Data pre-processing started at:", time_data_prep_start)
import DataPrep
time_train_start = time.time()
print("Model training started at:", time_train_start)
import Model

BATCH_SIZE = 32
EPOCHS = 20

fitted_model = Model.model.fit_generator(DataPrep.prep_train,
                                         steps_per_epoch=DataPrep.SAMPLE_SIZE*(1-DataPrep.TEST_RATIO)/BATCH_SIZE,
                                         epochs=EPOCHS,
                                         validation_data=DataPrep.prep_test,
                                         validation_steps=DataPrep.SAMPLE_SIZE*(DataPrep.TEST_RATIO/BATCH_SIZE))

Model.model.save(filepath=DataPrep.DATASET_DIR + 'trained_model.h5')
Model.model.save_weights(filepath=DataPrep.DATASET_DIR + 'trained_model_weights.h5')
time_end = time.time()
print("Training complete")
print("Data pre-processing time:", time_train_start - time_data_prep_start)
print("Model training time:", time_end - time_train_start)


import matplotlib.pyplot as plt


path = 'results'
name = 'adam'

plt.plot(fitted_model.history['acc'])
plt.plot(fitted_model.history['val_acc'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper left')

plt.show()

plt.figure()
plt.gcf().clear()
plt.plot(fitted_model.history['loss'])
plt.plot(fitted_model.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper left')

plt.show()

