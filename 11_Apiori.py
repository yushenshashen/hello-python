'''
date: 2018-12-23
goal: eleventh chapter Apriori
author: zp
'''

import math
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1( dataSet ):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                c1.append([item])
    C1.sort()
    C1 = map(frozenset, C1)
    return C1

def scanD( D, Ck, minSupport ):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                # if not ssCnt.has_key(can):
                if can not in ssCnt.keys():
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = len(ssCnt)
    retList = []
    supportData = {}
    for key in ssCnt.keys():
        support = ssCnt[support] / numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData

def aprioriGen( Lk, k ):
    retList = []
    for i in range(len(Lk)):
        for j in range(i+1,len(Lk)):
            L1 = Lk[i][:k-2]
            L2 = Lk[j][:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append( Lk[i] | Lk[j] )
    return retList

def apriori( dataSet, minSupport = 0.5 ):
    C1 = createC1(dataSet)
    D = map( set, dataSet )
    L1, supportData = scanD( D, C1, minSupport )
    L = [L1]
    k = 2
    while len(L[k-2]) > 0:
        Ck = aprioriGen(L[k-2], k )
        Lk, supK = scanD( d, Ck, minSupport )
        supportData.update( supK )
        L.append( Lk )
        k += 1
    return L, supportData

# generate the association rules
def generateRules(L, supportData, minConf=0.7):
    bigRuleLists = []
    for i in range(1,len(L)):
        for freqSet in L[i]:
            H1 = [ frozenset([item]) for item in freqSet ]
            if i > 1:
                resultsFromConseq( freqSet, H1, supportData, bigRuleLists, minConf )
            else:
                calConf( freqSet, H1, supportData, bigRuleLists, minConf )
    return bigRuleLists

def calConf( freqSet, H, supportData, brl, minConf=0.7 ):
    prunedH = []
    fro conseq in H:
    conf = supportData[ freqSet ] / supportData[ freqSet-conseq ]
    if conf > minConf:
        brl.append( (freqSet-conseq, conseq, conf) )
        prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    m = len(H[0])
    if len(freqSet) > m+1:
        Hmp1 = aprioriGen( H,m+1 )
        Hmp1 = calConf( freqSet, Hmp1, supportData, brl, minConf )
        if len(Hmp1)>1:
            rulesFromConseq( freqSet, Hmp1,supportData, brl, minConf )

