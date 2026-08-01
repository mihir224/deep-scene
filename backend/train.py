from tensorflow.keras.preprocessing.image import ImageDataGenerator
from model import Meso4

generator_config = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='nearest'
)

train_generator = generator_config.flow_from_directory(
    './Dataset/Train',
    target_size=(256, 256),
    batch_size=32,
    class_mode='binary'
)

validation_generator = generator_config.flow_from_directory(
    './Dataset/Validation',
    target_size=(256, 256),
    batch_size=32,
    class_mode='binary'
)

model = Meso4()

model.fit(train_generator, validation_generator, epochs=40)

model.save('model_weights.h5')

print("Training Complete.")
