from PIL import Image
from keras.src.datasets import mnist
from tensorflow.keras.models import load_model
from utils import dataloader as d
from models import cnn_model as c
def digit_recogniser_func():
    retrain()


def predict(image):
    image = Image.open(image)
    model = load_model('models/mnist.keras')
    predict=c.cnn_model()
    prediction=predict.predict_image(image, model)
    return(prediction)



def retrain():
    recogniser = d.dataloader()
    recogniser.load_mnist_data()
    recogniser.normalization()
    x_train, x_test, y_train, y_test = recogniser.reshape()

    cnn = c.cnn_model()
    cnn.build_cnn_model()
    cnn.train_cnn_model(x_train, y_train, x_test, y_test)

if __name__ == "__main__":
    digit_recogniser_func()

