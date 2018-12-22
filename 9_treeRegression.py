'''
date: 2018-12-22
goal: ninth chapter tree regression
author: zp
'''

import math
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(fltLine)
    return dataMat

testMat = np.mat(np.eye(4))
print(testMat)

def binSplitData( dataset, feature, value ):
# dataset = testMat
# featre =1
# value =0.5
    mat0 = dataset[np.nonzero(dataset[:,feature] > value)[0],:]
    mat1 = dataset[np.nonzero(dataset[:,feature] <= value)[0],:]
    return mat0,mat1

def regLeaf(dataset):
    # dataset = np.mat(dataset)
    return np.mean(dataset[:,-1])

def regErr(dataset):
    return np.var(dataset[:,-1]) * np.shape(dataset)[0]

def createTree(dataset, leafType=regLeaf, errType=regErr,ops=(1,4)):
    feat,val = chooseBestSplit( dataset, leafType, errType, ops )
    if feat == None:
        return val
    retTree = {}
    retTree['spInd'] = feat
    retTree['spVal'] = val
    lSet,rSet = binSplitData( dataset, feat, val )
    retTree['left'] = createTree( dataset, leafType, errType, ops )
    retTree['right'] = createTree(dataset, leafType, errType, ops)
    return retTree

def chooseBestSplit( dataset, leafType=regLeaf, errType=regErr, ops=(1,4) ):
# dataset = testMat
# leafType = regLeaf
# errType = regErr
# ops=(1,4)
    tolS = ops[0]
    tolN = ops[1]

    if len(set(dataset[:,-1].T.tolist()[0])) == 1:
        return None, leafType(dataset)
    m,n = np.shape(dataset)
    S = errType(dataset)

    bestS = np.inf; bestIndex = 0; bestVal = 0
    for featIndex in range(n-1):
        for splitVal in set(dataset[:,featIndex].T.tolist()[0]):
            mat0, mat1 = binSplitData( dataset, featIndex, splitVal )
            if( np.shape(mat0)[0] < tolN ) or (np.shape(mat1)[0]<tolN):
                continue
            newS = errType(mat0) + errType(mat1)
            if newS < bestS:
                bestS = newS
                bestIndex = featIndex
                bestVal = splitVal

    if (S - bestS) < tolS:
        return None, leafType(dataset)
    mat0,mat1= binSplitData(dataset, bestIndex, bestVal)
    if (len(mat0) < tolN ) or (len(mat1) < tolN ):
        return None, leafType(dataset)
    return bestIndex, bestVal

myTree = createTree( testMat, leafType=regLeaf, errType = regErr, ops=(1,4))

myDat = loadDataSet('rawdata/Ch09/ex00.txt')
myDat = np.mat(myDat)
# print(myDat)
myTree = createTree( myDat )
print(myTree)

def isTree(obj):
    return ( type(obj).__name__ == 'dict' )
def getMean( tree ):
    if isTree( tree['left'] ):
        tree['left'] = getMean(tree['left'])
    if isTree( tree['right'] ):
        tree['right'] = getMean(tree['right'])
    return ( tree['left'] + tree['right'] ) / 2.0

def prune( tree, testData ):
    if np.shape(testData)[0] == 0:
        return getMean( tree )
    if isTree( tree['left'] ) or isTree(tree['right']):
        lSet, rSet = binSplitData(testData, tree['spInd'], tree['spVal'])
    if isTree(tree['left']):
        tree['left'] = prune(tree['left'], lSet)
    if isTree(tree['right']):
        tree['right'] = prune( tree['right'], rSet )
    if not isTree( tree['left'] ) and not isTree(tree['right']):
        lSet, rSet = binSplitData( testData, tree['spInd'], tree['spVal'])
        errNoMerge = sum( np.power(lSet[:,-1]-tree['left'], 2) ) + sum( np.power(rSet[:,-1]-tree['right'], 2) )
        treeMean = ( tree['left'] + tree['right'] ) / 2.0
        errMerge = sum( np.power(testData[:,-1]-treeMean, 2) )
        if errMerge <- errNoMerge:
            print('merging')
            return treeMean
        else:
            return tree

def linearSolve(dataSet):
    m,n = np.shape(dataSet)
    X = np.mat(np.ones(m,n))
    Y = np.mat(np.ones((m,1)))
    X[:,1:n] = dataSet[:,0:(n-1)]
    Y = dataSet[:,-1]
    xTx = X.T* X
    if np.linalg.det( xTx )==0.0:
        raise NameError('singular can not inverse')
    ws = xTx.I * (X.T * Y)
    return ws, X, Y

def modelLeaf(dataSet):
    ws, X, Y = linearSolve(dataSet)
    return ws

def modelErr(dataSet):
    ws, X, Y = linearSolve(dataSet)
    yHat = X * ws
    return sum( np.power(Y-yHat,2) )

#use the tree to predict
def regTreeEval(model, inData):
    return float(model)

def modelTreeEval(model, inData):
    n = np.shape(inData)
    X = np.ones( (1,n+1) )
    X[:,1:] = inData
    return float(X * model)

def treeForeCast( tree, inData, modelEval=regTreeEval ):
    if not isTree(tree):
        return modelEval(tree, inData)
    if inData[tree['spInd']] > tree['spVal']:
        if isTree(tree['left']):
            return treeForeCast(tree['left'], inData, modelEval)
        else:
            return modelEval(tree['left'], inData)
    else:
        if isTree(tree['right']):
            return treeForeCast(tree['right'], inData, modelEval)

def createForeCast( tree, testData, modelEval = regTreeEval ):
    m = len(testData)
    yHat = np.zeros( (m,1) )
    for i in range(m):
        yHat[i] = treeForeCast( tree, testData[i,:], modelEval )
    return yHat

