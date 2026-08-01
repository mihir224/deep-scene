from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D, BatchNormalization, Dropout, Reshape, \
    LeakyReLU
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Model

image_dimensions = {'height': 256, 'width': 256, 'channels': 3}


class Classifier:
    def __init__(self):
        self.model = 0

    def predict(self, x):
        return self.model.predict(x)

    def fit(self, train_generator, validation_generator, epochs=10):
        self.model.fit(
            train_generator,
            steps_per_epoch=train_generator.samples // train_generator.batch_size,
            epochs=epochs,
            validation_data=validation_generator,
            validation_steps=validation_generator.samples // validation_generator.batch_size
        )

    def get_accuracy(self, x, y):
        return self.model.test_on_batch(x, y)

    def load(self, path):
        self.model.load_weights(path)

    def save(self, path):
        self.model.save_weights(path)

    def evaluate(self, test_generator):
        return self.model.evaluate(test_generator)
class Meso4(Classifier):
    def __init__(self, learning_rate=0.001):
        self.model = self.init_model()
        optimizer = Adam(lr=learning_rate)
        self.model.compile(optimizer=optimizer,
                           loss='binary_crossentropy',
                           metrics=['accuracy'])

    def init_model(self):
        x = Input(shape=(image_dimensions['height'],
                         image_dimensions['width'],
                         image_dimensions['channels']))

        x1 = Conv2D(8, (3, 3), padding='same', activation='relu')(x)
        x1 = BatchNormalization()(x1)
        x1 = MaxPooling2D(pool_size=(2, 2), padding='same')(x1)

        x2 = Conv2D(8, (5, 5), padding='same', activation='relu')(x1)
        x2 = BatchNormalization()(x2)
        x2 = MaxPooling2D(pool_size=(2, 2), padding='same')(x2)

        x3 = Conv2D(16, (5, 5), padding='same', activation='relu')(x2)
        x3 = BatchNormalization()(x3)
        x3 = MaxPooling2D(pool_size=(2, 2), padding='same')(x3)

        x4 = Conv2D(16, (5, 5), padding='same', activation='relu')(x3)
        x4 = BatchNormalization()(x4)
        x4 = MaxPooling2D(pool_size=(4, 4), padding='same')(x4)

        # 2 additional convolutional layers
        x5 = Conv2D(32, (3, 3), padding='same', activation='relu')(x4)
        x5 = BatchNormalization()(x5)
        x5 = MaxPooling2D(pool_size=(2, 2))(x5)

        x6 = Conv2D(64, (3, 3), padding='same', activation='relu')(x5)
        x6 = BatchNormalization()(x6)
        x6 = MaxPooling2D(pool_size=(2, 2))(x6)

        y = Flatten()(x6)
        y = Dropout(0.5)(y)

        y = Dense(64)(y)
        y = LeakyReLU(alpha=0.1)(y)
        y = Dropout(0.5)(y)

        y = Dense(1, activation='sigmoid')(y)

        return Model(inputs=x, outputs=y)
