'''
date: 2018-12-17
goal: seventh chapter adaboost
author: zp
'''

import math
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def loadSimpData():
    datMat = np.matrix([[ 1. ,  2.1],
        [ 2. ,  1.1],
        [ 1.3,  1. ],
        [ 1. ,  1. ],
        [ 2. ,  1. ]])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat,classLabels

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split('\t')) #get number of fields
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat-1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

datMat, classLabels = loadSimpData()
print(datMat)
print(classLabels)

def stumpClassify(dataMatrix, dimen,threshVal, threshIneq):
    retArry = np.ones(shape(dataMatrix)[0],1)
    if threshIneq == 'lt':
        retArry[dataMatrix[:,dimen] <= threshVal] = -1.0
    else:
        retArry[ dataMatrix[:,dimen] > thresVal ] = -1.0
    return retArry

def buildStump(dataArr, classLabels,D):
    dataMatrix = np.mat(dataArr)
    labelMat = np.mat(classLabels).T
    m,n = np.shape(dataMatrix)
    numSteps = 10
    bestStump = {}
    bestClassEst = np.mat(np.zeros((m,1)))
    minError = inf
    for i in range(n):
        rangeMin = dataMatrix[:,i].min()
        rangeMax = dataMatrix[:.i].max()
        stepSize = (rangeMax- rangeMin)/numSteps
        for j in range( -1, int(numSteps)+1 ):
            for inequal in ['lt','gt']:
                threshVal = rangeMin + float(j) * stepSize
                predictedVals = stumpClassify(dataMatrix, i,threshVal, inequal)
                errArr = np.mat(np.ones((m,1)))
                errArr[ predictedVals== labelMat ] = 0
                weightedError = D.T * errArr
                if weightedError < minError:
                    minError = weightedError
                    bestClassEst = predictedVals.copy() # as to numpy should think of copy
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestClassEst

def adBoostTrainDS(dataArr, classLabels,numIter=40):
    weekClassArr = []
    m,n = np.shape(dataArr)
    D = np.mat(np.ones((m,1))/m)
    aggClassEst = np.mat(np.zeros((m,1)))
    for i in range(numIter):
        bestStump, error, classEst = buildStump( dataArr, classLabels,D )
        alpha = float(0.5*np.log( (1.0-error)/max(error, 1e-16) ))
        bestStump['alpha'] = alpha
        weekClassArr.append( bestStump )

        expon = np.multiply( -1*  alpha*np.mat(classLabels).T, classEst )
        D = np.multiply( D, expon )
        D = D / D.sum()
        aggClassEst += alpha*classEst

        aggErrors = np.multiply( np.sign(aggClassEst)!=np.mat(classLabels).T, np.ones((m,1)) )
        errorRate = aggErrors.sum()/m

        if errorRate == 0:
            break
    return weekClassArr

