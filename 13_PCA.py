'''
date: 2018-12-24
goal: thirteenth chapter PCA
author: zp
'''

import math
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fr = open('rawdata/Ch13/testSet.txt')
delim='\t'
# for line in fr.readlines()[:5]:
    # print(line.strip().split(delim))
stringArr = [ line.strip().split(delim) for line in fr.readlines()]
dataArry = [ [float(x) for x in line ] for line in stringArr]
dataMat = np.mat(dataArry)
print(dataMat[:5])
print(np.shape(dataMat))
def pca(dataMat, topNfeat=9999):
    # topNfeat = 9999
    meanVals = np.mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals
    print(meanRemoved[:5])
    covMat = np.cov(meanRemoved, rowvar=0)
    print(covMat[:5])
    print(np.shape(covMat))
    eigVals, eigVects = np.linalg.eig(np.mat(covMat))
    print(eigVals)
    print(np.shape(eigVals))
    print(eigVects)
    print(np.shape(eigVects))
    eigValIndex = np.argsort(eigVals)
    print(eigValIndex)
    eigValIndex = eigValIndex[:-(topNfeat+1):-1]
    redEigVects = eigVects[:,eigValIndex]
    lowDataMat = meanRemoved * redEigVects
    reconMat = (lowDataMat * redEigVects.T) + meanVals
    # print(lowDataMat)
    # print(reconMat)
    return lowDataMat, reconMat

lowDMat, reconMat = pca( dataMat,1 )
print(lowDMat[:5])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter( dataMat[:,0].flatten().A[0], dataMat[:,1].flatten().A[0], marker='o',c='red' )
ax.scatter(reconMat[:,0].flatten().A[0],reconMat[:,1].flatten().A[0],marker='x',c='blue')
# plt.show()

fr = open('rawdata/Ch13/secom.data')
stringArr = [ line.strip().split(' ') for line in fr.readlines() ]
# dataArry = [ map(float, line) for line in stringArr ]
dataArry = [ [float(x) for x in line ] for line in stringArr ]
dataMat = np.mat(dataArry)
print(dataMat[:5])
numFeat = np.shape(dataMat)[1]
# for i in range(numFeat):
i = 1
# print(  dataMat[np.nonzero(~np.isnan(dataMat[:5,i])),i]  )
meanVal = np.mean(dataMat[np.nonzero(~np.isnan(dataMat[:,i]))[0],i])
print(meanVal)
dataMat[np.nonzero(np.isnan(dataMat[:,i]))[0],i] = meanVal
