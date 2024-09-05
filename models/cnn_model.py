import numpy as np
from PIL import ImageOps
from keras.src.legacy.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt


class cnn_model:
    def __init__(self):
        self.cnn_model1=None
        self.image_input_shape = (28,28,1)
        self.num=10

    def build_cnn_model(self):
        self.cnn_model1=Sequential()
        self.cnn_model1.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=self.image_input_shape))
        self.cnn_model1.add(MaxPooling2D(pool_size=(2, 2)))
        self.cnn_model1.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
        self.cnn_model1.add(MaxPooling2D(pool_size=(2, 2)))
        self.cnn_model1.add(Flatten())
        self.cnn_model1.add(Dense(128, activation='relu'))
        self.cnn_model1.add(Dropout(0.5))
        self.cnn_model1.add(Dense(self.num, activation='softmax'))

        self.compile_cnn_model()

    def compile_cnn_model(self):
        self.cnn_model1.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    def check_results (self,x_test,y_test):
        result =self.cnn_model1.evaluate(x_test,y_test)
        print("The loss of this is : ",result[0])
        print("The accuracy of this is : ", result[1])

    def create_combined_dataset(self, x_train, y_train):
        x_train_inverted = self.invert_colors(x_train)
        x_train_combined = np.concatenate((x_train, x_train_inverted), axis=0)
        y_train_combined = np.concatenate((y_train, y_train), axis=0)

        return x_train_combined, y_train_combined

    def invert_colors(self, image):
        return 1-image
    def train_cnn_model(self, x_train, y_train, x_test, y_test):
        x_train, y_train = self.create_combined_dataset(x_train, y_train)

        y_train = to_categorical(y_train, num_classes=self.num)
        y_test = to_categorical(y_test, num_classes=self.num)


        datagen = ImageDataGenerator(
            rotation_range=5,
            width_shift_range=0.1,
            height_shift_range=0.1,
            shear_range=0.1,
            zoom_range=0.1,
            fill_mode='nearest',
            horizontal_flip=False

        )
        hist = self.cnn_model1.fit(datagen.flow(x_train, y_train, batch_size=44),epochs=10,validation_data=(x_test, y_test))
        print("The model has successfully trained")
        self.cnn_model1.save('mnist.keras')
        self.check_results(x_test,y_test)

    def predict_image(self, image,model):

        image = image.convert('L')

        image = image.resize((28, 28))
        image= np.array(image)

        image = image.astype('float32')/ 255.00
        image = image.reshape(1, 28, 28, 1)
        plt.imshow(image[0, :, :, 0], cmap='gray')
        plt.title("Processed Image")
        plt.show()
        result =model.predict(image)



        print(result)
        predicted_result = np.argmax(result, axis=1)
        return predicted_result[0]



















