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


test_generator = generator_config.flow_from_directory(
    './Dataset/Test',
    target_size=(256, 256),
    batch_size=32,
    class_mode='binary',
    shuffle=False
)


model = Meso4()


evaluation = model.evaluate(test_generator)


print("Test Loss:", evaluation[0])
print("Test Accuracy:", evaluation[1])