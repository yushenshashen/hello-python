'''
date: 2018-12-17
goal: sixth chapter SVM
author: zp
'''

import math
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#simple version

def loadDataSet(fileName):
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

def selectJ(i,m):
    j = i
    while j == i:
        j = int(np.random.uniform(0, m))
    return j

def clipAlpha(aj,H,L):
    if aj > H:
        aj = H
    if aj < L:
        aj = L
    return aj

dataArr, labelArr = loadDataSet('rawdata/Ch06/testSet.txt')
print(dataArr[:5])
print(labelArr[:5])

smoSimple( dataMatrix, classLabels, C, toler, maxIter ):
    # C = 0.6
    # toler = 0.001
    # maxIter = 10
    dataMatrix = np.mat(dataArr)
    labelMat = np.mat(labelArr).transpose()
    print(np.shape(dataMatrix))
    print(np.shape(labelMat))
    b= 0
    m,n = np.shape(dataMatrix)
    iter= 0
    alphas = np.mat(np.zeros( (m,1) ))
    print(alphas[:5])
    print(type(alphas))
    while iter < maxIter:
        alphaPairsChanged = 0
        for i in range(m):
            # i = 1
            fXi = float( np.multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[i,:].T ) ) + b
            Ei= fXi - float(labelMat[i])
            if ((labelMat[i]*Ei < -toler) and (alphas[i]<C)) or ((labelMat[i]*Ei > toler) and (alphas[i]>0)):
                j = selectJ(i, m)
                fXj = float(np.multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[j, :].T)) + b
                Ej = fXj - labelMat[j]
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                if labelMat[i] != labelMat[j]
                    L = max(0, alphas[j]-alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0,alphas[i] + alphas[j]-C)
                    H= min(C, alphas[i]+alphas[j])

                if L==H:
                    print('L==H')
                    continue
                eta = 2 * dataMatrix[i,:]* dataMatrix[j,:].T - dataMatrix[i,:] * dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0:
                    print('eta>=0')
                    continue
                alphas[j] -= labelMat[j]* (Ei-Ej)/eta
                alphas[j] = clipAlpha(alphas[j],H,L)
                if( abs(alphas[i]-alphas[j])< 0.0001 ):
                    print('moving too little')
                    continue
                alphas[i] += labelMat[i]*labelMat[j]*(alphaJold-alphas[j])

                b1 = b - Ei -
                b2 = b - Ej -
                if(0<alphas[i]) and (alphas[i]<C):
                    b =b1
                elif (0<alphas[j]) and (alphas[j]<C):
                    b= b2
                else:
                    b= (b1+b2)/2.0
                alphaPairsChanged +=1

        if (alphaPairsChanged==0):
            iter += 1
        else:
            iter = 0
    return b, alphas

#complete version of SMO
class optStruct:
    def __init__(self, dataMatIn, classLabels, C, toler):
        self.X= dataMatIn
        self.C = C

        self.eCache = np.mat(np.zeros((self.m,2)))

def clacEk(os,k):
    fXk = float( np.multiply(os.alphas, os.labelMat).T * (os.X * os.X[k,:].T) ) + os.b
    Ek = fXk - float( self.labelMat[k] )
    return Ek

def selectJ(i, os, Ei):
    maxK = -1; maxDeltaE = 0; Ej = 0
    os.eCache[i] = [1,Ei]
    validEcacheList = np.nonzero(os.eCache[:,0].A)[0]  # .A change to array  nonzero get the index of nonzero value
    if len(validEcacheList) > 1:
        for k in validEcacheList:
            if k == i:
                continue
            Ek = calcEk(oS, k)
            detaE = abs(Ei-Ek)
            if detaE > maxDeltaE:
                maxK= k
                maxDeltaE = detaE
                Ej = k
        return maxK,Ej
    else:
        j = selectJrand(i, oS.m)
        Ej = calcEk(oS,j)
    return j,Ej

def kernelTrans(X, A, kTup):
    m,n = np.shape(X)
    K= np.mat(zeros((m,1)))
    if kTup[0] == 'lin':
        K = X * A.T
    elif kTup[0] == 'rbf':
        for j in range(m):
            deltaRow = X[j,:] - A
            K[j] = deltaRow * deltaRow.T
        K = np.exp( K / (-1*kTup[2]**2) )
    else:
        raise NameError('not recognized')

    return K

# def testRbf(k1 =1.3):
dataArr,labelArr = loadDataSet('rawdata/Ch06/testSetRbf.txt')
b, alphas = smoP( dataArr, labelArr, C=200, toler=0.0001, maxIter=10000 )
dataMat = np.mat(dataArr)
labelMat = np.mat(labelArr).transpose()
svInd = np.nonzero(alphas.A>0)[0]
sVs = dataMat[svInd]
labelSV = labelMat[svInd]
print('there are {} suport vets'.format(np.shape(sVs)[0]))
m,n = np.shape(dataMat)
errorCount = 0
for i in range(m):
    kernelEval = kernelTrans(sVs, dataMat[i,:],('rbf',k1))
    predictResult = kernelEval * np.multiply(labelSV, alphas[svInd]) + b
    if np.sign(predictResult) != np.sig(labelMat[i]):
        errorCount += 1


