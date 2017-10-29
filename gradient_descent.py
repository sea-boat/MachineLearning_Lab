import numpy as np
import matplotlib.pyplot as plt

learning_rate = 0.0005
theta = [0.7, 0.8, 0.9]
loss = 100
times = 100
ite = 0
expectation = 0.0001
x_train = [[1, 2], [2, 1], [2, 3], [3, 5], [1, 3], [4, 2], [7, 3], [4, 5], [11, 3], [8, 7]]
y_train = [7, 8, 10, 14, 8, 13, 20, 16, 28, 26]
loss_array = np.zeros(times)


def h(x):
    return theta[0]*x[0]+theta[1]*x[1]+theta[2]

while loss > expectation and ite < times:
    loss = 0
    sum_theta0 = 0
    sum_theta1 = 0
    sum_theta2 = 0
    for x, y in zip(x_train, y_train):
        sum_theta0 += (h(x) - y) * x[0]
        sum_theta1 += (h(x) - y) * x[1]
        sum_theta2 += (h(x) - y)
    theta[0] -= learning_rate * sum_theta0
    theta[1] -= learning_rate * sum_theta1
    theta[2] -= learning_rate * sum_theta2

    loss = 0
    for x, y in zip(x_train, y_train):
        loss += pow((h(x) - y), 2)
    loss_array[ite] = loss
    ite += 1

plt.plot(loss_array)

plt.show()
