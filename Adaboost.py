import numpy as np
import matplotlib.pyplot as plt

np.random.seed(111)


def weak_model(data, Dt):
    m = data.shape[0]
    pred = []
    pos = None
    mark = None
    min_err = np.inf
    for j in range(m):
        pred_temp = []
        sub_mark = None
        print(data[:j, 1])
        print(data[j:, 1])
        lsum = np.sum(data[:j, 1])
        rsum = np.sum(data[j:, 1])
        if lsum < rsum:
            sub_mark = -1
            pred_temp.extend([-1.] * (j))
            pred_temp.extend([1.] * (m - j))
        else:
            sub_mark = 1
            pred_temp.extend([1.] * (j))
            pred_temp.extend([-1.] * (m - j))
        err = np.sum(1 * (data[:, 1] != pred_temp) * Dt)
        if err < min_err:
            min_err = err
            pos = (data[:, 0][j - 1] + data[:, 0][j]) / 2
            mark = sub_mark
            pred = pred_temp[:]
    model = [pos, mark, min_err]
    return model, pred


def adaboost(data):
    models = []
    N = data.shape[0]
    D = np.zeros(N) + 1.0 / N
    M = 3
    y = data[:, -1]
    for t in range(M):
        Dt = D[:]
        model, y_ = weak_model(data, Dt)
        errt = model[-1]
        alpha = 0.5 * np.log((1 - errt) / errt)
        Zt = np.sum([Dt[i] * np.exp(-alpha * y[i] * y_[i]) for i in range(N)])
        D = np.array([Dt[i] * np.exp(-alpha * y[i] * y_[i]) for i in range(N)]) / Zt
        models.append([model, alpha])
    return models


def predict(models, X):
    pred = []
    for x in X:
        result = 0
        for base in models:
            alpha = base[1]
            if x[0] > base[0][0]:
                result -= base[0][1] * alpha
            else:
                result += base[0][1] * alpha
        pred.append(np.sign(result))
    return pred


if __name__ == "__main__":
    data = np.array([[0, 1], [1, 1], [2, 1], [3, -1], [4, -1], [5, -1], [6, 1], [7, 1], [8, 1], [9, -1]],
                    dtype=np.float32)
    models = adaboost(data)
    X = data
    Y = data[:, -1]
    Y_ = predict(models, X)
    acc = np.sum(1 * (Y == Y_)) / float(len(X))
    print(acc)
