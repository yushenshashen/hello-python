# code: utf-8
#date: 2018-12-14
#goal: fourth chapter naive Bayes

import math
from collections import Counter
import numpy as np
from numpy import *

def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec

listOPosts, listClasses = loadDataSet()

print(listOPosts)

##way 1 get unique vocab
vocablist = []
[ vocablist.extend(x) for x in listOPosts ]
myVocab = set(vocablist)
print(sorted(myVocab))
print(len(myVocab))

#way2
def createVocab(dataset):
    voc = []
    for example in dataset:
        voc = set(voc) | set(example)
    return list(voc)
    # print(sorted(voc))
    # print(len(voc))

def setOfWords2Vec( vocabList, inputSet ):
    vec=  [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            vec[ vocabList.index(word) ] = 1
        else:
            print('not inside')
    return vec

myVocab = createVocab( listOPosts )
print(myVocab)
print(myVocab.index('stupid'))

trainMatrix = []
for each in listOPosts:
    trainMatrix.append(setOfWords2Vec(myVocab, each))
print(trainMatrix)
trainCategory = listClasses
print(trainCategory)

def trainNB0(trainMatrix, trainCategory):
    numTrain = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pA = sum(trainCategory) / float(numTrain)
    p1Num = np.zeros(numWords)
    p0Num = np.zeros(numWords)
    p1Sum = 0
    p0Sum = 0
    for i in range(numTrain):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Sum += sum(trainMatrix[i])
        elif trainCategory[i] == 0:
            p0Num += trainMatrix[i]
            p0Sum += sum(trainMatrix[i])
    p1Vect = p1Num / p1Sum
    p0Vect = p0Num / p0Sum

    return p1Vect, p0Vect, pA
# print([p1Vect,p0Vect, pA])
# print(myVocab[p1Vect.argmax()])


def classfyNB( vecTest,p1Vec, p0Vec, pA ):
    p1 = sum(vecTest * p1Vec) + log(pA)
    p0 = sum(vecTest * p0Vec) + log(1-pA)
    if p1 > p0:
        return 1
    else:
        return 0

p1Vec,p0Vec,pA = trainNB0(trainMatrix, trainCategory)
testEntry = ['I','love','my','dog']
testArray = np.array( setOfWords2Vec( myVocab, testEntry ) )
print(testArray)
predictLabe = classfyNB( testArray, p1Vec,p0Vec, pA)
print(predictLabe)
testEntry = ['stupid','dog']
testArray = np.array( setOfWords2Vec( myVocab, testEntry ) )
print(testArray)
predictLabe = classfyNB( testArray, p1Vec,p0Vec, pA)
print(predictLabe)

def bagOFWords2Vec( vocabList, inputSet ):
    returnVec = [0] * len(vocabList)
    for each in inputSet:
        if each in vocabList:
            returnVec[ vocabList.index(each) ] += 1
    return returnVec

##classify the email
import re
import random

# regrex = re.compile(r'\w+')
# words = regrex.findall(emailText )
# print(words)
emailText = open('rawdata/Ch04/email/spam/1.txt','r').read()
print(emailText)

def textParse( bigString ):
    words = re.findall(r'[A-Za-z]+', bigString)
    parsedWords = [ x.lower() for x in words if len(x) >= 3 ]
    return parsedWords

import os

spamFile = os.listdir('rawdata/Ch04/email/spam/')
hamFile = os.listdir('rawdata/Ch04/email/ham')

spamList = []
for each in spamFile:
    text = open( 'rawdata/Ch04/email/spam/' + each,'r' ).read()
    content = textParse(text)
    spamList.append(content)

hamList = []
for each in hamFile:
    text = open('rawdata/Ch04/email/ham/'+each,'r').read()
    content = textParse(text)
    hamList.append(content)

docList = spamList + hamList
print(docList)
docLabels = [1] * len(spamList) + [0] * len(hamList)
print(docLabels)
vocabList = createVocab( docList )
print(vocabList)

testIndex = random.sample(range(0,len(docList)),10)
trainIndex = [ x for x in range(0,len(docList)) if x not in testIndex ]
print(testIndex)
print(trainIndex)

trainData = []
trainLabel = []
for i in trainIndex:
    trainData.append( setOfWords2Vec( vocabList, docList[i] ) )
    trainLabel.append( docLabels[i] )

p1V, p0V, pSpam = trainNB0( trainData, trainLabel )

errorCount = 0
for i in testIndex:
    testData = setOfWords2Vec(vocabList, docList[i])
    testLabel = docLabels[i]
    testResult = classfyNB(testData, p1V,p0V,pSpam)

    print( 'the real label is {}, the predict result is {}'.format( testLabel, testResult ) )
    if testResult == testLabel:
        pass
    else:
        errorCount += 1

errorRatio = float(errorCount) / len(testIndex) * 100
print( 'the error ratio is {:.3f}%'.format(errorRatio) )

##RSS from ads analysis diff city
import feedparser

