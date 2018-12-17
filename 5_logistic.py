#date: 2018-12-14
#goal: fifth chapter logistic

import math
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##the way to get multiple index from list
#b = [7, 8, 3, 2, 3, 4, 5, 3]
#[ i for i,j in enumerate(b) if j == 3]

dataArr = []
labelMat = []
f =open('rawdata/Ch05/testSet.txt','r')
for line in f.readlines():
    line = line.strip().split()
    dataArr.append([1.0,float(line[0]),float(line[1])])
    labelMat.append( int(line[2]) )

print(dataArr[:5])
print(labelMat[:5])

def sigmoid(inx):
    return 1.0 / (1 + np.exp(-inx) )

def stockGradAscent(dataArr, classLabels):
    dataMatrix =np.mat( dataArr )
    labelMatrix = np.mat(labelMat).transpose()
    m,n = dataMatrix.shape
    maxCycle = 500
    alpha = 0.001
    weights = np.ones((n,1))
    for k in range(maxCycle):
        error = sigmoid( dataMatrix * weights ) - labelMatrix
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights

# plot the divide line
def plotline():
    dataMatrix = dataArr
    print(dataMatrix[:5])
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(m):
        if int(labelMat[i]) == 1:
            xcord1.append(dataMatrix[i,1])
            ycord1.append(dataMatrix[i,2])
        else:
            xcord2.append( dataMatrix[i,1] )
            ycord2.append( dataMatrix[i,2] )

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter( xcord1, ycord1, c='r' )
    ax.scatter( xcord2, ycord2, c='b' )
    x = np.arange(-3.0,3.0,0.1).reshape(1,60)
    y = (-weights[0]-weights[1] * x) / weights[2]
# print(x)
# print(x.shape)
# print(y)
# print(y.shape)
# print(weights)
# print(weights.shape)
# ax.plot(x,y)
# plt.show()

# random choose a sample
def stockGradAscent0(dataMatrix, classLabels):
    m,n = shape(dataMatrix)
    alpha = 0.01
    weights =np.ones((1,n))
    for i in range(m):
        h = sigmoid( sum(dataMatrix[i]*weights) )
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]
    return weights

dataMatrix = np.array(dataArr)
classLabels = labelMat
print(dataMatrix[:5])
print(classLabels[:5])

def stockGradAscents1( dataMatrix, classLabels, numIter = 150 ):
    m,n = np.shape(dataMatrix)
    weights = np.ones(n)
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4 / (1+j+i) + 0.01
            randIndex = int( np.random.uniform(0,len(dataIndex)) )
            h = sigmoid( sum(dataMatrix[randIndex]*weights) )
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del dataIndex[randIndex]
    return weights

def classifyVec(inx, weights):
    prob = sigmoid( sum(inx * weights) )
    if prob >= 0.5:
        return 1.0
    else:
        return 0.0

frTrain = pd.read_table('rawdata/Ch05/horseColicTraining.txt',sep='\t',header=None)
trainSet = np.array(frTrain.iloc[:,:21])
trainLabels = list(frTrain.iloc[:,21])
print(frTrain[:5])
print(np.shape(frTrain))
print(np.shape(trainSet))
print(trainLabels[:5])
trainWeights = stockGradAscents1( np.array(trainSet), trainLabels, numIter=500 )
print(trainWeights)

errorCount = 0
testCount = 0
f = open('rawdata/ch05/horseColicTest.txt','r')
for line in f.readlines():
    line = line.strip()
    testCount += 1
    testData = line.split('\t')[:21]
    [float(x) for x in testData ]
    testLabel = line.split('\t')[21]
    # print(line)
    # print(testData)
    # print(testLabel)
    predictLabel = classifyVec(np.array(testData,dtype='float'), trainWeights)
    # print(predictLabel)
    if int(predictLabel) != int(testLabel):
        errorCount += 1

errorRate = float(errorCount) / testCount * 100
print(errorRate)