from numpy import *

dataSet = [[0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [1, 0], [0, 0], [1, 0], [1, 0], [1, 1], [1, 0], [1, 1],
           [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
ySet = [0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]


def train():
    dataNum = len(dataSet)
    featureNum = len(dataSet[0])
    p0Num = ones(featureNum)
    p1Num = ones(featureNum)
    p0Denom = 2.0
    p1Denom = 2.0
    p0 = 0
    for i in range(dataNum):
        if ySet[i] == 1:
            p1Num += dataSet[i]
            p1Denom += sum(dataSet[i])
        else:
            p0 += 1
            p0Num += dataSet[i]
            p0Denom += sum(dataSet[i])
    p0Rate = p0 / dataNum
    p0Vec = log(p0Num / p0Denom)
    p1Vec = log(p1Num / p1Denom)
    return p0Rate, p0Vec, p1Vec


p0Rate, p0Vec, p1Vec = train()
test = [1, 0]
p1 = sum(test * p1Vec) + log(1.0 - p0Rate)
p0 = sum(test * p0Vec) + log(p0Rate)
if p1 > p0:
    print(1)
else:
    print(0)
