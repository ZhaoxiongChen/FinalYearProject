# Environment-installed packages
import os  # os - System libraries
from keras.preprocessing.image import ImageDataGenerator  # Keras Pre-processing libraries

# Set up pre-processing configurations by initializing ImageDataGenerator class
# rescale - normalisation 0-255 to 0-1
# zoom_range & h/v flip - reduce position sensitive while training models
# shear_range - reduce shape sensitive while training models
preprocess_config = ImageDataGenerator(rescale=1./255)
augmentation_config = ImageDataGenerator(rescale=1./255, zoom_range=0.2, horizontal_flip=True, vertical_flip=True,
                                         shear_range=0.2)


def prep_exec(config, input_df, batch_size, side_length):

    """This function generates pre-processed image iterator, which is the source of augmented images
       Images will NOT be saved in this method."""

    prep_result = config.flow_from_dataframe(
        dataframe=input_df,
        directory=os.path.dirname(input_df['Directory'].values[0]),
        x_col='Directory',
        y_col='HasShip',
        target_size=(side_length, side_length),
        color_mode='rgb',
        class_mode='sparse',
        batch_size=batch_size,
        shuffle=True
    )

    return prep_result
