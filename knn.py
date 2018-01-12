from numpy import *
import pylab as pl

dataSet = array([[11, 12], [12, 12], [11, 11], [11, 16], [12, 16], [17, 11], [17, 12]])
classes = ['A', 'A', 'A', 'B', 'B', 'C', 'C']
k = 3
dot = [13, 13]
type
r = 0
dataSize = dataSet.shape[0]
diff = tile(dot, (dataSize, 1)) - dataSet
sqdiff = diff ** 2
squareDist = sum(sqdiff, axis=1)
dist = squareDist ** 0.5
sortedDistIndex = argsort(dist)
classCount = {}
for i in range(k):
    label = classes[sortedDistIndex[i]]
    classCount[label] = classCount.get(label, 0) + 1
    if dist[i] > r:
        r = dist[i]
maxCount = 0
for key, value in classCount.items():
    if value > maxCount:
        maxCount = value
        type = key
pl.plot(dot[0], dot[1], 'ok')
circle = [i * pi / 180 for i in range(0, 360)]
x = cos(circle) * r + dot[0]
y = sin(circle) * r + dot[1]
pl.plot(x, y, 'r')
pl.plot([point[0] for point in dataSet[0:3]], [point[1] for point in dataSet[0:3]], 'og')
pl.plot([point[0] for point in dataSet[3:5]], [point[1] for point in dataSet[3:5]], 'or')
pl.plot([point[0] for point in dataSet[5:7]], [point[1] for point in dataSet[5:7]], 'oy')
pl.show()
