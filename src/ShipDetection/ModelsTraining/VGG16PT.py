# PT == "Pre-trained"
# This VGG16 model employs pre-trained parameter provided by keras.
# http://...

from keras.applications.vgg16 import VGG16
from keras.layers import Dropout, Flatten, Dense
from keras.models import Model

raw_vgg16 = VGG16(weights='imagenet', include_top=False, input_shape=(256, 256, 3), pooling='max')

for layer in raw_vgg16.layers:
    layer.trainable = False

x = raw_vgg16.output
x = Dense(4096, activation='relu')(x)
x = Dropout(0.5)(x)
x = Dense(4096, activation='relu')(x)
x = Dropout(0.5)(x)
out = Dense(1, activation='sigmoid')(x)

# DEPRECATED: out = Dense(1, activation='softmax')(x)

# creating the final model
model = Model(input=raw_vgg16.input, output=out)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()
