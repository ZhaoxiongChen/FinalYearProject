import time
import DataPrep as dp
import importlib

EPOCHS = 20

scale = dp.scale_select
if scale == "Sample_50k":
    data_size = 50000

else:
    data_size = dp.raw_data.shape[0]

model_name = dp.model_select
model = importlib.import_module("ModelsTraining." + model_name)

# Time start
t0_formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
t0 = time.process_time()
print("Model training started at:", t0_formatted)

fitted_model = model.model.fit_generator(generator=dp.prep_train,
                                         steps_per_epoch=data_size*(1-dp.TEST_RATIO)/dp.BATCH_SIZE,
                                         epochs=EPOCHS,
                                         validation_data=dp.prep_test,
                                         validation_steps=data_size*(dp.TEST_RATIO/dp.BATCH_SIZE),
                                         verbose=2)

# Time end
t1 = time.process_time()
t1_formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
date = time.strftime("%Y-%m-%d_", time.localtime())
print("Training complete")
print("Model training finished at:", t1_formatted)
print("Model training time:", t1 - t0)

model.model.save(filepath=dp.DATASET_DIR + date + model_name + "_trained_model.h5")
model.model.save_weights(filepath=dp.DATASET_DIR + date + model_name + 'trained_model_weights.h5')
