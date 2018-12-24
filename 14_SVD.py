'''
date: 2018-12-24
goal: fourteenth chapter PSVD
author: zp
'''

import math
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def loadExData():
    return[[0, 0, 0, 2, 2],
           [0, 0, 0, 3, 3],
           [0, 0, 0, 1, 1],
           [1, 1, 1, 0, 0],
           [2, 2, 2, 0, 0],
           [5, 5, 5, 0, 0],
           [1, 1, 1, 0, 0]]

def loadExData2():
    return[[0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
           [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
           [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
           [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
           [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
           [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
           [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
           [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
           [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
           [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
           [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]]

Data = loadExData()
print(np.shape(Data))
U, sigma, VT = np.linalg.svd( Data )
print(U)
print(sigma)
print(VT)

##three ways cal similarity
def eludSim(inA,inB):
    return 1.0/ (1.0+np.linalg.norm(inA-inB))

def pearsSim(inA, inB):
    if len(inA) < 3:
        return 1.0
    else:
        return 0.5+0.5*np.corrcoef( inA,inB,rowvar=0 )[0][1]

def cosSim(inA,inB):
    num = float(inA.T*inB)
    denom = np.linalg.norm(inA) * np.linalg.norm(inB)
    return 0.5+0.5*(num/denom)

##recommend dished
myMat = loadExData()
print(myMat)

def standEst( dataMat,user, simMeans, item ):
    n = np.shape(dataMat)[1]
    simTotal = 0.0
    rateSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating == 0:
            continue
        overlap = np.nonzero(logical_and(dataMat[:,item].A>0, dataMat[:,j].A>0))
        if len(overlap) == 0 :
            similarity = 0
        else:
            similarity = simMeans( dataMat[overlap,item], dataMat[overlap, j] )
        simTotal += similarity
        rateSimTotal += similarity * rateSimTotal
    if simtotal == 0:
        return 0
    else:
        return rateSimTotal / similarity

def recommend(dataMat, user, N=3,simMeas=cosSim, estMethod=standEst):
    unratedItem = np.nonzero(dataMat[user,:].A==0)[1]
    if len(unratedItem) == 0:
        print('you rated everything')
    itemScores = []
    for item in unratedItem:
        estimatedScore = estMethod( dataMat, user, simMeas, item )
        itemScores.append((item,estimatedScore))
    sortedItems = sorted(itemScores, key=lambda x:x[1], reverse=True)
    return sortedItems

dataSet = np.mat(loadExData2())
print(dataSet)
U, Sigma,VT = np.linalg.svd(dataSet)
print(Sigma)

print(sum(Sigma**2))
print(sum(Sigma[:3]**2))
dataMat = np.mat(loadExData())
print(dataMat)

def svdEst(dataMat, user, simMeas, item):
    n = np.shape(dataMat)[1]
    simTol= 0
    rateSimTotal = 0.0
    U,sigma, VT = np.linalg.svd( dataMat )
    Sig4 = np.mat(np.eye(4)*sigma[:4])
    xformedItems = dataMat.T * U[:,:4] * Sig4
    for j in range(n):
        userRating = dataMat[user, j]
        if userRating == 0 or j == item:
            continue
        similarity = simMeas( xformedItems[item,:].T, xformedItems[j,:].T )
        simTol += similarity
        rateSimTotal += similarity * userRating

    if simTol == 0:
        return 0
    else:
        return rateSimTotal / simTol

U, sigma, VT = np.linalg.svd(dataMat)
Sig4 = np.mat(np.eye(4)*sigma[:4])
xformedItems = dataMat.T * U[:,:4] * Sig4
print(xformedItems)
# print(np.shape(U))
# print(VT)
# print(np.shape(VT))
print( U[:,:4] * Sig4 * VT[:4,:] )

def printMat( inMat, thresh=0.8 ):
    for i in range(32):
        for k in range(32):
            if float(inMat[i,k]) > thresh:
                print(1)
            else:
                print(0)
        print(' ')

# def imgCompress( numSV=3, thresh=0.8 ):
myl = []
f = open('rawdata/Ch14/0_5.txt')
for line in f.readlines():
    new_row = []
    for i in range(32):
        new_row.append( int(line[i]) )
    myl.append(new_row)
myMat = np.mat(myl)
print(myMat[:5])

U, Sigma, VT = np.linalg.svd( myMat )
SigRen = np.mat(np.zeros((3,3)))
for k in range(3):
    SigRen[k,k] = Sigma[k]
print(SigRen)
print(np.shape(Sigma[:3]))
print(np.mat(np.eye(3)*Sigma[:3]))
reconMat = U[:,:3] * SigRen * VT[:3,:]
print(reconMat[:5])