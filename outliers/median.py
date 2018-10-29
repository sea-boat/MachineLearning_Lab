import numpy as np
import matplotlib.pyplot as plt


def get_median_filtered(signal, threshold=3):
    difference = np.abs(signal - np.median(signal))
    median_difference = np.median(difference)
    s = 0 if median_difference == 0 else difference / float(median_difference)
    mask = s > threshold
    signal[mask] = np.median(signal)
    return signal


with open('../data/data.txt') as f:
    data = [float(c.strip()) for c in f.readlines()]
    plt.figure(1)
    plt.subplot(211)
    plt.scatter(range(len(data)), data, marker='.', alpha=0.5)

    window_size = 10
    median_filtered_signal = []

    for ii in range(0, len(data), window_size):
        median_filtered_signal += get_median_filtered(np.asanyarray(data[ii: ii + window_size])).tolist()

    plt.subplot(212)
    plt.scatter(range(len(median_filtered_signal)), median_filtered_signal)

    plt.show()
