import numpy as np


step = lambda x: 1 if x > 0 else 0


class Perceptron:
    def __init__(self, activation=step):
        self.weights = None
        self.activation = activation

    def fit(self, X, y, size, epochs=10, alpha=0.1):
        # initialize weights
        self.weights = np.random.rand(size + 1) / np.sqrt(size)

        # add bias to the input
        X = np.c_[X, np.ones(X.shape[0])]

        # run epochs
        for epoch in range(epochs):
            for x, target in zip(X, y):
                # prediction is dot product of input and weights
                # passed through activation function
                pred = self.activation(np.dot(x, self.weights))

                # update weights
                if pred != target:
                    error = pred - target
                    self.weights += -alpha * error * x

    def predict(self, X):
        X = np.atleast_2d(X)
        X = np.c_[X, np.ones(X.shape[0])]
        return self.activation(np.dot(X, self.weights))
