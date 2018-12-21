'''
date: 2018-12-21
goal: eighth chapter regression
author: zp
'''

import math
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

xArry, yArry = loadDataSet('rawdata/Ch08/ex0.txt')
print(xArry)
print(type(xArry))
print(yArry)

def standRegre( xArry, yArry ):
    xMat = np.mat(xArry)
    yMat = np.mat(yArry).T

    # print( np.shape(xArry) )
    xTx = xMat.T * xMat
    if np.linalg.det( xTx )==0:
        print('the mat is siglular, cannot do inverse')
        return
    ws = xTx.I * xMat.T * yMat
    return ws

ws = standRegre( xArry, yArry )

xMat = np.mat(xArry)
yMat = np.mat(yArry)
yHat = xMat * ws

fig = plt.figure()
ax = fig.add_subplot(111)
# print(xMat[:,1].flatten().A[0])
ax.scatter( xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0] )

print(xMat[:5,:])
#way 1 two way of sort for numpy remember axis 0 1
xCopy =  xMat
xCopy.sort(0)
yHat = xCopy * ws
ax.plot( xCopy[:,1], yHat )
# plt.show()

# way 2
xNew = np.sort(xMat,0)
yHat = xNew * ws
ax.plot( xNew[:,1], yHat )
# print(np.sort(xMat,0)[:5,:])

print( np.corrcoef( yHat.T, yMat ) ) # only for 1X100


# locally weighted linear regression
#     testPoint = xArry[0]
#     k=1.0

def lwlr( testPoint, xArry, yArry, k=1.0 ):
    xMat = np.mat(xArry)
    yMat = np.mat(yArry).T
    m,n = np.shape(xMat)
    weights = np.mat( np.eye(m) )
    for j in range(m):
        diffMat = testPoint - xMat[j,:]
        weights[j,j] = np.exp( diffMat * diffMat.T / (-2.0 * k ** 2) )

    xTx = xMat.T * ( weights* xMat )
    if np.linalg.det(xTx) == 0:
        print('singerular can not reverse')
        # return
    # print( np.shape(xTx.I) )
    # print( np.shape(weights * yMat) )
    ws = xTx.I * (xMat.T * ( weights * yMat))
    return testPoint * ws

test0 = lwlr( xArry[0], xArry, yArry, k=1.0 )
print(test0)

def lwlrTest( testArry, xArry, yArry, k=1.0 ):
    # testArry = xArry
    m,n = np.shape( testArry )
    yHat = np.zeros(m)
    for j in range(m):
        yHat[j] = lwlr( testArry[j], xArry, yArry, k )
    return yHat

yHat = lwlrTest( xArry, xArry, yArry, k=0.003 )
print(yHat[:10])

xMat = np.mat(xArry)
print(xMat[:10,:])

sortIndex = xMat[:,1].argsort(0)
xSorted = xMat[sortIndex][:,0,:]
print(xSorted[:10,: ])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot( xSorted[:,1].tolist(), yHat[sortIndex].tolist(),c='r' )
ax.scatter( xMat[:,1].tolist(), yArry )
# plt.show()
#
# 对于X[:,:,0]
# 是取三维矩阵中第一维的所有数据
# 对于X[:,:,1]
# 是取三维矩阵中第二维的所有数据
# 对于X[:,:,m:n]
# 是取三维矩阵中第m维到第n-1维的所有数据

def rssError(yArry, yHatArry):
    return ((yArry - yHatArry)**2).sum()

def ridgeRes( xMat, yMat,lam=0.2 ):
    # xMat = np.mat(xArry)
    # yMat = np.mat(yArry).T
    # lam = 0.2
    xTx = xMat.T * xMat
    m,n = np.shape(xMat)
    demo = xTx + np.eye( n ) * lam
    if np.linalg.det(demo) == 0:
        print('singular')
    ws = demo.I * (xMat.T * yMat)
    return ws

abX, abY = loadDataSet('rawdata/Ch08/abalone.txt')
print(abX[:10])
print(abY[:10])

def ridgeTest( xArry, yArry ):
    xMat = np.mat( abX )
    yMat = np.mat( abY ).T
    # print( np.shape(xMat) )
    m,n = np.shape(xMat)

    # print(yMat[:5])
    # print(yMat.mean())
    yMean = np.mean(yMat,0)  #the same with yMat.mean()
    yMat = yMat - yMean
    xMean = np.mean( xMat, 0 )
    xVar = np.var( xMat,0 )
    xMat = (xMat-xMean ) / xVar
    numTest = 30
    wMat = np.zeros( (numTest, n) )
    for i in range(numTest):
        ws = ridgeRes( xMat, yMat, lam=np.exp(i-10) )
        wMat[i] = ws.T
    return wMat

ridgeWeights = ridgeTest( abX, abY )
print(ridgeWeights[:5,:])

plt.plot(ridgeWeights)
# plt.show()

def regularize( inMat ):
    xMean = np.mean( inMat, 0 )
    xVar = np.var( inMat,0 )
    xMat = (inMat-xMean ) / xVar
    return xMat

#forward step regression

# def stageWise(abX, abY,eps=0.01, numIt = 100):
eps = 0.01
numIt = 100
xMat = np.mat(abX)
yMat = np.mat(abY).T
m,n = np.shape(xMat)
yMean = np.mean( yMat,0 )
yMat = yMat - yMean
xMat = regularize( xMat )
returnMat= np.zeros( (numIt, n) )
ws = np.zeros((n,1)); wsTest = ws.copy(); wsMax = ws.copy()
for i in range( numIt ):
    print( ws.T )
    lowestError = np.inf
    for j in range( n ):
        for sign in [-1,1]:
            wsTest = ws.copy()
            wsTest[j] += eps* sign
            yTest = xMat * wsTest
            rssError = rssError(  yMat.A,yTest.A, )
            if rssError < lowestError:
                lowestError = rssError
                wsMax = wsTest

    ws = wsMax.copy()
    returnMat[i,:] = ws.T
# return returnMat
print(returnMat)

#logo toys
np.shape( lgX ) #58,4
lgX1 = np.mat( np.zeros((58,5)))
logX1[:,1:5] = logX

##crossvalidation
def crossValidation(xArry, yarry, numVal =10):
    m = len(xArry)
    indexList = range(m)
    errorMat = np.zeros( (numVal, 30) )
    for i in range(numVal):
        trainX= []; trainY= []
        testX = []; testY= []
        np.random.shuffle(indexList)
        for j in range(m):
            if j <= 0.9*m:
                trainX.append( xArry[indexList[j]] )
                trainY.append(yArry[indexList[j]])
            else:
                testX.append( xArry[indexList[j]] )
                testY.append(yArry[indexList[j]])
        wMat = ridgeTest( trainX , trainY) # 30* n
        for k in range(30):
            matTestX = np.mat(testX)
            matTrainX = np.mat( trainX )
            meanTrain = np.mean( matTrainX,0 )
            varTrain = np.var(matTrainX,0)
            matTestX = (matTestX- meanTrain) / varTrain
            yEst = matTestX * np.mat(wMat[k,:]).T + np.mean(trainY)
            errorMat[i,k] = rssError(yEst.T.A - np.array(yTest))
    meanErrors = np.mean(errorMat,0)
    minMean = min(meanErrors)
    bestWeights = wMat[ np.nonzero(meanErrors==minMean) ]
    xMat = np.mat(xArry)
    ymat = np.mat(yArry).T
    meanX = np.mean( xMat, 0 )
    varX = np.var( xMat, 0 )
    unReg = bestWeights / varX
    print('bestweights is{}'.format(unReg))
    constant = -1*sum( np.multiply(meanX, unReg) ) + np.mean(yMat)




