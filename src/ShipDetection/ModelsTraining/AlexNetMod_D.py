from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.layers.convolutional import Conv2D, MaxPooling2D

model = Sequential()

# Modified Dense Layer

# Conv1
model.add(Conv2D(filters=96, kernel_size=(11, 11), strides=(4, 4), activation='relu', padding='valid',
                 input_shape=(256, 256, 3)))
# Pool1
model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
# Conv2
model.add(Conv2D(filters=256, kernel_size=(5, 5), strides=(1, 1), activation='relu', padding='same'))
# Pool2
model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
# Conv3
model.add(Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
# Conv4
model.add(Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
# Conv5
model.add(Conv2D(filters=256, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding='same'))
# Pool5
model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
# Flatten
model.add(Flatten())
# FC6 + dropout
model.add(Dense(units=128, activation='relu'))
model.add(Dropout(0.01))
# FC7 + dropout
model.add(Dense(units=128, activation='relu'))
model.add(Dropout(0.01))
# FC8
model.add(Dense(units=1, activation='sigmoid'))
# Compile
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Summary
model.summary()

# Old name: AlexNetMod
# New name: AlexNetMod_D
