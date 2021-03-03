import time
import DataPrep as dp
import importlib
from Utilities import SelectionValidation as sv
from Utilities import TimeStamp as time_stamp

EPOCHS = 20

MODEL_MENU = "\nAvailable model to train:\n"
MODEL_DICT = {
              "CNN": "CNNBenchmark",
              "AlexNet": "AlexNet",
              "AlexNetMod_D": "AlexNetMod_D",
              "AlexNetMod_D_F": "AlexNetMod_D_F",
              "AlexNetMod_D_F_KS": "AlexNetMod_D_F_KS",
              "ResNetPT": "ResNet50PT",
              "VGG16": "VGG16",
              "VGG16Mod_D_F": "VGG16Mod_D_F",
              "VGG16PT": "VGG16PT"
              }

for key in MODEL_DICT:
    MODEL_MENU = MODEL_MENU + key + "\n"

input_validation = sv.SelectionValidation(selection_dict=MODEL_DICT,
                                          menu_message=MODEL_MENU,
                                          welcome_message="Please select a model:")


model_select = MODEL_DICT[input_validation.validation()]

scale = dp.scale_select
if scale == "Sampled":
    # data_size = 50000
    data_size = 25000

else:
    data_size = dp.raw_data.shape[0]

network_arch = importlib.import_module("ModelsTraining." + model_select)
model = network_arch.model

# Time start
time_stamp = time_stamp.TimeStamp()
time_stamp.start()

# Operation: Model training
history = model.fit_generator(generator=dp.prep_train,
                              steps_per_epoch=data_size*(1-dp.TEST_RATIO)/dp.BATCH_SIZE,
                              epochs=EPOCHS,
                              validation_data=dp.prep_test,
                              validation_steps=data_size*(dp.TEST_RATIO/dp.BATCH_SIZE),
                              verbose=1)

# Time finish
time_stamp.stop()
print("Training complete")

# Time summary
time_stamp.summary()
del time_stamp

# Saving results and histories
date = time.strftime("%Y-%m-%d_", time.localtime())
model.save(filepath=dp.dataset_dir + date + model_select + "_trained_model.h5")
model.save_weights(filepath=dp.dataset_dir + date + model_select + '_trained_model_weights.h5')
with open(date + model_select + '_history.txt', 'w') as file:
    file.write(str(history.history))

'''When using this layer as the first layer in a model, provide the keyword argument input_shape 
(tuple of integers, does not include the batch axis), e.g. input_shape=(128, 128, 3) 
for 128x128 RGB pictures in data_format="channels_last".'''
