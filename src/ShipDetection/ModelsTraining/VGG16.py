from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout


# Build a model
model = Sequential()


# Block 1 - 2 convolution layers
# conv1_1, relu1_1
model.add(Conv2D(filters=64, padding='same', strides=(1, 1), kernel_size=(3, 3), input_shape=(256, 256, 3),
                 activation='relu'))
# conv1_2, relu1_2
model.add(Conv2D(filters=64, padding='same', strides=(1, 1), kernel_size=(3, 3), activation='relu'))
# pool1
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))


# Block 2 - 2 convolution layers
# conv2_1, relu2_1
model.add(Conv2D(filters=128, padding='same', strides=(1, 1), kernel_size=(3, 3), activation='relu'))
# conv2_2, relu2_2
model.add(Conv2D(filters=128, padding='same', strides=(1, 1), kernel_size=(3, 3), activation='relu'))
# pool2
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))


# Block 3 - 3 convolution layers
# conv3_1, relu3_1
model.add(Conv2D(filters=256, padding='same', strides=(1, 1), kernel_size=(3, 3), activation='relu'))
# conv3_2, relu3_2
model.add(Conv2D(filters=256, padding='same', strides=(1, 1), kernel_size=(3, 3), activation='relu'))
# conv3_3, relu3_3
model.add(Conv2D(filters=256, padding='same', strides=(1, 1), kernel_size=(3, 3), activation='relu'))

# pool3
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))


# Block 4 - 3 convolution layers
# conv4_1, relu4_1
model.add(Conv2D(filters=512, padding='same', strides=(1, 1), kernel_size=(3, 3), activation='relu'))
# conv4_2, relu4_2
model.add(Conv2D(filters=512, padding='same', strides=(1, 1), kernel_size=(3, 3), activation='relu'))
# conv4_3, relu4_3
model.add(Conv2D(filters=512, padding='same', strides=(1, 1), kernel_size=(3, 3), activation='relu'))
# pool4
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))


# Block 5 - 3 convolution layers
# conv5_1, relu5_1
model.add(Conv2D(filters=512, padding='same', strides=(1, 1), kernel_size=(3, 3), activation='relu'))
# conv5_2, relu5_2
model.add(Conv2D(filters=512, padding='same', strides=(1, 1), kernel_size=(3, 3), activation='relu'))
# conv5_3, relu5_3
model.add(Conv2D(filters=512, padding='same', strides=(1, 1), kernel_size=(3, 3), activation='relu'))
# pool5
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))


# Convert into 1 dimension, prepare for FC layers
model.add(Flatten())


# Block 6 - full connection layer
# fc6, relu6,
model.add(Dense(units=4096, activation='relu'))
# drop6
model.add(Dropout(0.5))


# Block 7 - full connection layer
# fc7, relu7,
model.add(Dense(units=4096, activation='relu'))
# drop7
model.add(Dropout(0.5))


# Block 8 - full connection layer
# fc8
model.add(Dense(units=1, activation='softmax'))


# Summary & Compile
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

model.summary()
