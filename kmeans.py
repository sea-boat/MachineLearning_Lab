from numpy import *
import matplotlib.pyplot as plt

_dataset = [[1, 1], [3, 1], [1, 4], [2, 5], [11, 12], [14, 11], [13, 12], [11, 16], [17, 12], [28, 10], [26, 15],
            [27, 13], [28, 11], [29, 15]]
dataset = mat(_dataset)
k = 3
sampleNum, col = dataset.shape
cluster = mat(zeros((sampleNum, 2)))
centroids = zeros((k, col))
mark = ['or', 'ob', 'og']


def kmeans():
    # choose centroids
    for i in range(k):
        index = int(random.uniform(0, sampleNum))
        centroids[i, :] = dataset[index, :]
    cluster_changed = True
    while cluster_changed:
        cluster_changed = False
        for i in range(sampleNum):
            min_dist = sqrt(sum(power(centroids[0, :] - dataset[i, :], 2)))
            min_index = 0
            for j in range(1, k):
                distance = sqrt(sum(power(centroids[j, :] - dataset[i, :], 2)))
                if distance < min_dist:
                    min_dist = distance
                    min_index = j
            if cluster[i, 0] != min_index:
                cluster_changed = True
                cluster[i, :] = min_index, min_dist ** 2
        for j in range(k):
            points_in_cluster = dataset[nonzero(cluster[:, 0].A == j)[0]]
            centroids[j, :] = mean(points_in_cluster, axis=0)
    return centroids, cluster


centroids, cluster = kmeans()
for i in range(sampleNum):
    markIndex = int(cluster[i, 0])
    plt.plot(dataset[i, 0], dataset[i, 1], mark[markIndex])

mark = ['+r', '+b', '+g']
for i in range(k):
    plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize=12)

plt.show()
