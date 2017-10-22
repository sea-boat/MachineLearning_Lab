import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 11.5, 12, 13, 14.5, 15.5, 16.8, 17.3, 18, 18.7]

A = np.vstack([x, np.ones(len(x))]).T

a, b = np.linalg.lstsq(A, y)[0]
print("y = %10.5fx + %10.5f" % (a, b))
x = np.array(x)
y = np.array(y)

plt.plot(x, y, 'o', label='data', markersize=10)
plt.plot(x, a * x + b, 'r', label='line')
plt.show()
