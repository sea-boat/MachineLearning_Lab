import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

dataSet = [[1, 1], [3, 1], [1, 4], [2, 5], [11, 12], [14, 11], [13, 12], [11, 16], [17, 12], [28, 10], [26, 15],
           [27, 13], [28, 11], [29, 15]]
dataSet = np.mat(dataSet)
cls = DBSCAN(eps=5, min_samples=3).fit(dataSet)
markers = ['^', 'o', 'x']
clusterNum = len(set(cls.labels_))
for i in range(clusterNum):
    members = cls.labels_ == i
    plt.scatter(dataSet[members, 0].tolist(), dataSet[members, 1].tolist(), marker=markers[i])
plt.show()
