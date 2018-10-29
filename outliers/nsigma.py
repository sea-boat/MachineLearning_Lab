import matplotlib.pyplot as plt
import numpy as np

with open('../data/data.txt') as f:
    data = [float(c.strip()) for c in f.readlines()]

    plt.figure(1)
    plt.subplot(311)
    plt.hist(data)

    plt.subplot(312)
    plt.plot(data)

    plt.subplot(313)
    x = range(0, len(data))
    plt.plot(x, data)
    mu = np.mean(data)
    sigma = np.std(data)
    n_sigma = 3
    markers = []
    marker_indexs = []
    i = 0
    for c in data:
        i += 1
        if c > (mu + n_sigma * sigma) or c < (mu - n_sigma * sigma):
            markers.append(c)
            marker_indexs.append(i)
    plt.plot(marker_indexs, markers, 'g.', label='tps', marker='o', alpha=0.5, markersize=8)
    plt.show()


