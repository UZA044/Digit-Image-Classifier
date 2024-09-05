from tensorflow.keras.datasets import mnist


class dataloader:
    def __init__(self):
        self.x_train=None
        self.x_test =None
        self.y_train=None
        self.y_test=None

    def load_mnist_data(self):
        (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data()

    def normalization(self):
        self.x_train=self.x_train/255
        self.x_test=self.x_test/255

    def reshape(self):
        self.x_train = self.x_train.reshape(self.x_train.shape[0], 28, 28, 1)
        self.x_test = self.x_test.reshape(self.x_test.shape[0], 28, 28, 1)
        return self.x_train, self.x_test, self.y_train , self.y_test



