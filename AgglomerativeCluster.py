import numpy as nu
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

dataSet = [[1, 1], [3, 1], [1, 4], [2, 5], [1, 2], [3, 2], [2, 4], [1, 5], [11, 12], [14, 11], [13, 12], [11, 16],
           [17, 12], [12, 12], [11, 11], [14, 12], [12, 16], [17, 11], [28, 10], [26, 15], [27, 13], [28, 11], [29, 15],
           [29, 10], [26, 16], [27, 14], [28, 12], [29, 16], [29, 17], [29, 13], [26, 18], [27, 13], [28, 11], [29, 17]]
dataSet = nu.mat(dataSet)
clusterNum = 3
cls = AgglomerativeClustering(linkage='ward', n_clusters=clusterNum).fit(dataSet)
markers = ['^', 'o', 'x']
for i in range(clusterNum):
    members = cls.labels_ == i
    plt.scatter(dataSet[members, 0], dataSet[members, 1], marker=markers[i])
plt.show()
