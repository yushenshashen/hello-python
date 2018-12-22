'''
date: 2018-12-22
goal: tenth chapter K mean
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

def distEclud( vecA, vecB ):
    dist = np.sqrt( sum( np.power(vecA - vecB,2) ) )
    return dist

def randCent( dataSet, k ):
    m,n = np.shape(dataSet)
    centroids = np.mat( np.zeros((k,n)) )
    for i in range(n):
        minI = min( dataSet[:,i] )
        maxI = max( dataSet[:,i] )
        rangeI = maxI - minI
        centroids[:,i] = minI + rangeI * np.random.rand(k,1)
    return centroids

dataMat = loadDataSet( 'rawdata/Ch10/testSet.txt' )

def kmeans( dataSet, k, distMeas = distEclud, createCent = randCent ):
# dataSet = dataMat
# k= 4
# distMeas = distEclud
# createCent = randCent
    dataSet = np.mat(dataSet)
    m,n = np.shape( dataSet )
    clusterAssment = np.zeros( (m,2) )
    centroids = np.zeros((k,n))
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = np.inf
            minIndex = 0
            for j in range(k):
                dist = distMeas( dataSet[i,:], centroids[j,:] )
                if dist < minDist:
                    minIndex = j
                    minDist = dist
            if clusterAssment[i, 0] == minIndex:
                clusterAssment[i,:] = minIndex, minDist**2
            else:
                clusterChanged = True

        for cent in range(k):
            oneClusterMat = dataSet[ np.nonzero(clusterAssment[:,0].A == cent)[0] ]
            centroids[cent,:] = np.mean(oneClusterMat,0)

        return centroids, clusterAssment

myDat = kmeans( dataMat, 4 )
print(myDat)

def biKmean( dataSet, k, distMeas=distEclud ):
    m = np.shape(dataSet)[0]
    clussterAssment = np.mat(np.zeros((m,2)))
    centroid0 = np.mean( dataSet, axis=0 ).tolist()[0]
    centList = [ centroid0 ]
    for j in range(m):
        clussterAssment[j,1] = distMeas( centroid0, dataset[j,:] )**2
    while len(centList) < k:
        lowestSSE = np.inf
        for i in range( len(centList) ):
            oneCluster = dataSet[ np.nonzero(clussterAssment[:,0].A==i)[0],: ]
            centroidMat, splitClustAss = kmeans( oneCluster, 2, distMeas )
            sseSplit = sum( splitClustAss[:,1] )
            sseNoSplit = sum( clussterAssment[ np.nonzero(clussterAssment[:,0]!=i)[0],1 ] )
            if (sseSplit + sseNoSplit) < lowestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit = sseNoSplit

        bestClustAss[ np.nonzero(bestClustAss[:,0]==1)[0],0 ] = len(centList)
        bestClustAss[ np.nonzero( bestClustAss[:,0]==0 )[0],0 ] = bestCentToSplit

        centList[ bestCentToSplit ] = bestNewCents[0,:]
        centList.append( bestNewCents[1,:] )
        clussterAssment[ np.nonzero(clussterAssment[:,0].A == bestCentToSplit)[0],: ] = bestClustAss
    return np.mat(centList), clussterAssment
