import numpy as np
from nns import Perceptron


def main():
    # Logical AND
    # 0 0 -> 0
    # 0 1 -> 0
    # 1 0 -> 0
    # 1 1 -> 1
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [0], [0], [1]])

    print('Training...')
    nn = Perceptron()
    nn.fit(X, y, X.shape[1])

    print('Testing...')
    for x, t in zip(X, y):
        pred = nn.predict(x)
        print(f'input: {x}, expected: {t}, predicted: {pred}')


if __name__ == '__main__':
    main()
