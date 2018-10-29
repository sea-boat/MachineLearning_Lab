import numpy as np
import matplotlib.pyplot as plt
import random

# signal
number_of_samples = 1000
frequency = 5
sample_time = 0.001
amplitude = 1
s_time = [ii * sample_time for ii in range(number_of_samples)]

# noise
mu = 0
sigma = 1


def bandpass_filter(x, freq, frequency_of_signal=frequency, band=0.05):
    if (frequency_of_signal - band) < abs(freq) < (frequency_of_signal + band):
        return x
    else:
        return 0


def simulate():
    plt.figure(1)
    plt.subplot(511)
    signal = [amplitude * np.sin((2 * np.pi) * frequency * ii * sample_time) for ii in range(number_of_samples)]
    plt.plot(s_time, signal)
    plt.annotate('原始信号', xy=(0, 0))
    noise = [random.gauss(mu, sigma) for _ in range(number_of_samples)]
    plt.subplot(512)
    # plt.plot(noise)
    plt.hist(noise)
    plt.annotate('噪音直方图', xy=(-3, 100))

    signal_with_noise = [ii + jj for ii, jj in zip(signal, noise)]
    plt.subplot(513)
    plt.plot(s_time, signal_with_noise)
    plt.annotate('有噪信号', xy=(0, 0))

    fft_of_signal_with_noise = np.fft.fft(signal_with_noise)
    f = np.fft.fftfreq(len(fft_of_signal_with_noise), sample_time)
    plt.subplot(514)
    plt.plot(f, abs(fft_of_signal_with_noise), '.')
    plt.annotate('频率响应', xy=(-500, 100))

    F_filtered = np.asanyarray([bandpass_filter(x, freq) for x, freq in zip(fft_of_signal_with_noise, f)])
    filtered_signal = np.fft.ifft(F_filtered)
    plt.subplot(515)
    plt.plot(s_time, filtered_signal)
    plt.annotate('去燥信号', xy=(0, 0))
    plt.show()


def detect_outlier_position_by_fft(signal, threshold_freq=1, frequency_amplitude=.01):
    fft_of_signal = np.fft.fft(signal)
    outlier = np.max(signal) if abs(np.max(signal)) > abs(np.min(signal)) else np.min(signal)
    if np.any(np.abs(fft_of_signal[threshold_freq:]) > frequency_amplitude):
        index_of_outlier = np.where(signal == outlier)
        return index_of_outlier[0]
    else:
        return None


def detect_by_fft():
    with open('../data/data.txt') as f:
        data = [float(c.strip()) for c in f.readlines()]
        plt.figure(1)
        outlier_positions = []
        window = 100
        for ii in range(window, len(data), window):
            outlier_position = detect_outlier_position_by_fft(data[ii - window:ii + window])
            if outlier_position is not None:
                outlier_positions.append(ii + outlier_position[0] - window)
        outlier_positions = list(set(outlier_positions))
        plt.scatter(range(len(data)), data)
        plt.scatter(outlier_positions, np.array(data)[outlier_positions])
        plt.legend()
        plt.show()


if __name__ == '__main__':
    detect_by_fft()
