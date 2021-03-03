# PT == "Pre-trained"
# This ResNet50 model employs pre-trained parameter provided by keras.
# http://...

from keras.applications.resnet50 import ResNet50
from keras.layers import Dropout, Flatten, Dense
from keras.models import Model

raw_resnet = ResNet50(weights='imagenet', include_top=False, input_shape=(256, 256, 3))

for layer in raw_resnet.layers:
    layer.trainable = False

x = raw_resnet.output
x = Flatten()(x)
x = Dense(1024, activation='relu')(x)
x = Dropout(0.5)(x)
x = Dense(1024, activation='relu')(x)
out = Dense(1, activation='sigmoid')(x)
# DEPRECATED: out = Dense(1, activation='softmax')(x)

# creating the final model
model = Model(input=raw_resnet.input, output=out)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

