#date: 2018-12-14
#goal: second chapter decision tree

import math
from collections import Counter

myDat = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
labels = [ 'no surfacing', 'flippers' ]

def calShannonEnt( dataSet ):
    localLabels = [ x[-1] for x in dataSet ]
    labelsDict = {}
    # for i in localLabels:
    #     labelsDict[i] = labelsDict.get(i,0) + 1

    labelsDict = Counter(localLabels)
    shannonEnt = 0
    for k,v in labelsDict.items():
        p = float(v) / len(localLabels)
        shannonEnt += -p * math.log( p , 2)

    return shannonEnt

print( calShannonEnt(myDat) )

dataSet = myDat
axis = 0
value = 1

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featureVec in dataSet:
        if featureVec[axis] == value:
            # featureVec.remove(value)
            featureVec = featureVec[:axis] + featureVec[axis:]
            retDataSet.append(featureVec )
    return retDataSet

print( splitDataSet(myDat, 0,1) )

def chooseBestFeature(dataSet):
    numFeatures = len(dataSet[0])-1
    baseEnt = calShannonEnt(dataSet)
    bestInforGain= 0
    bestFeature = 1
    for i in range(numFeatures):
        allFeatures = [ x[i] for x in dataSet ]
        uniqueVals = set(allFeatures)
        newEnt = 0
        for value in uniqueVals:
            # print([i,value])
            subData = splitDataSet(dataSet, i, value)
            # print(subData)
            # subShannonEnt = calShannonEnt(subData)
            # print(subShannonEnt)
            prob = len(subData) / len(dataSet)
            newEnt += prob * calShannonEnt(subData)
        diffEnt = baseEnt - newEnt
        if diffEnt > bestInforGain:
            bestInforGain = diffEnt
            bestFeature = i

    return bestFeature

print(chooseBestFeature(myDat))

import operator

def createTree( dataSet, labels ):
    classList = [ x[-1] for x in dataSet ]
    if classList.count( classList[0] ) == len(classList): #used all the features but still can not split
        return classList[0]

    if len(dataSet[0]) == 1: # can not return the only label so choose the most frequence one
        classCount = {}
        for i in classList:
            classCount[i] = classCount.get(i,0) + 1
        sortedClassCount = sorted( classCount.items(), key = operator.itemgetter(1),reverse=True )
        return sortedClassCount[0][0]

    bestFeature = chooseBestFeature( dataSet )
    bestlabel = labels[bestFeature]

    myTree = { bestlabel: {} }
    del(labels[bestFeature])

    featureVal = [ x[bestFeature] for x in dataSet ]
    uniqueVal = set(featureVal)
    for value in uniqueVal:
        subLabel = labels[:]
        myTree[bestFeature][value] = createTree( splitDataSet(dataSet, bestFeature,value), subLabel )

    return myTree

#use decision tree
def classify( inputTree, featureLabels, testVec ):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featureIndex = featureLabels.index(firstStr)

    for key in secondDict.keys():
        if testVec(featureIndex) == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify( secondDict[key], featureLabels, testVec )
            else:
                classLabel = secondDict[key]

    return classLabel



