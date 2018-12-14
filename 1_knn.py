#date: 2018-12-11
#goal =: first chapter KNN

import numpy as np
import pandas as pd
import  operator
import matplotlib.pyplot as plt
import matplotlib

# film
#read in data
group = np.array([[1,1.1],[1,1],[0,0.1],[0,0.2]])
label = ['a','a','b','b']

# print(group)
plt.scatter(list(group[:,0]),list(group[:,1]))
# plt.show()

inX = [0,0]
# dataSet = group
# labels = label

def classify0( inX, dataSet, labels, k ):
    sigDataSet = (inX - dataSet)**2
    distances = sigDataSet.sum(axis=1)**0.5
    sortedDistanceIndex = distances.argsort()

    classCount = {}
    for i in range(k):
        voteLabel = labels[ sortedDistanceIndex[i] ]
        classCount[voteLabel] = classCount.get( voteLabel ,0 ) + 1

    sortedClassCount = sorted( classCount.items(), key = lambda x: x[1], reverse=True ) # or use lib operator key = opera  tor.itemgetter()
    return(sortedClassCount[0][0])

print(classify0([1,0], group, label, 3))

# hela dateing web
#
# f = open('rawdata/Ch02/datingTestSet.txt')
# matrix = []
# labels = []
# for line in f.readlines()[:5]:
#     line = line.strip()
#     line = line.split('\t')
#     matrix.append(line[:3])
#     labels.append(int(line[-1]))
#
# matrix = np.array(matrix,dtype=float)
#
# print(matrix[:3])
# print(labels[:5])

f = pd.read_table('rawdata/Ch02/datingTestSet2.txt', sep='\t',header=None)
matrix = f.iloc[:,:3]
datingDatMat= np.array(matrix)
datingLabels = list(f[3])

print(datingDatMat[:5])
print(datingLabels[:5])

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(  datingDatMat[:,1],datingDatMat[:,2], np.array(datingLabels), np.array(datingLabels) )
# plt.show()

#feature normalize
m = datingDatMat.shape[0]
datingMin = datingDatMat.min(axis=0)
datingMax = datingDatMat.max(axis=0)
datingMean = datingDatMat.mean(axis=0)
print(datingDatMat.min(axis=0))
print(np.tile(datingMin,(m,1))[:5])
print(datingDatMat.max(axis=0))
print(datingDatMat.mean(axis=0))

# normMat = datingDatMat.apply( get_normalization, axis=1 )
normMat = ( datingDatMat - np.tile(datingMean,(m,1)) ) / np.tile((datingMax - datingMin),(m,1))
print(normMat[:5])
testRatio = 0.1
testNum = int(m*0.1)
errorCount = 0
#
# for i in range(testNum):
#     classifyResult = classify0( normMat[i,:], normMat[testNum:,: ], datingLabels[testNum:],3 )
#     print( 'the classifor result is {} The true label is {}'.format( classifyResult , datingLabels[i]) )
#     if classifyResult != datingLabels[i]:
#         errorCount += 1
#
# print('the error rate is {}%' .format( float(errorCount) / testNum * 100 ))
# print( classify0(normMat[1,:], normMat, datingLabels, 3) )

# game = input('how long do you spent playing game:')

# imgDataMat = pd.read_table('rawdata/Ch02/digits/testDigits/0_13.txt',sep='',header=None)

# f = open('rawdata/Ch02/digits/testDigits/0_13.txt')


def img2vector(filename):
    f = open(filename,'r')
    # vec = []
    # for line in f.readlines():
    #     line = line.strip()
    #     vec.append(line)

    vec = f.readlines()
    vec = [ x.strip() for x in vec ]

    vec = list(''.join(vec) )
    vec = [ int(x) for x in vec ]
    return vec

testVec = img2vector( 'rawdata/Ch02/digits/testDigits/0_13.txt' )
print(testVec)

import os

def handwritingClass():
    trainingFiles = os.listdir('rawdata/Ch02/digits/trainingDigits')
    testFiles = os.listdir('rawdata/Ch02/digits/testDigits/')
    print(trainingFiles)
    print(testFiles)
    print(len(trainingFiles))
    print(len(testFiles))

    trainingLabels = []
    trainingData = []
    for i in trainingFiles:
        oneVec = img2vector( 'rawdata/Ch02/digits/trainingDigits/' + i )
        trainingData.append(oneVec)
        trainingLabels.append( int(i.split('_')[0]) )

    trainingData = np.array(trainingData)
    print(trainingData[:5])
    print(trainingLabels[:5])

    errorCount = 0
    for i in testFiles:
        testData = img2vector('rawdata/Ch02/digits/testDigits/' + i )
        testLabel = int( i.split('_')[0] )
        testResult = classify0( testData, trainingData, trainingLabels, 3 )

        if testResult != testLabel:
            errorCount += 1

    errorRatio = float(errorCount) / len(testFiles) * 100
    print('the error ratio is {:.2f}%'.format(errorRatio))
