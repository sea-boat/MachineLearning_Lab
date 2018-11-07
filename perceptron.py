import numpy as np

eta = 0.1
ite = 20


def train(x, y):
    w_ = np.zeros(1 + x.shape[1])
    for _ in range(ite):
        for xi, target in zip(x, y):
            update = eta * (target - predict(xi, w_))
            w_[1:] += update * xi
            w_[0] += update
    return w_


def predict(x, w):
    return np.where(np.dot(x, w[1:]) + w[0] >= 0, 1, -1)


x_train = np.array([[1, 2], [2, 1], [2, 3], [3, 5], [1, 3], [4, 2], [7, 3], [4, 5], [11, 3], [8, 7]])
y_train = np.array([1, 1, -1, -1, 1, -1, -1, 1, -1, 1])

w = train(x_train, y_train)
print("w = ", w)
x1 = [4, 3]
print(predict(x1, w))
