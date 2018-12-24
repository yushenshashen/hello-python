'''
date: 2018-12-23
goal: twelth chapter FP growth
author: zp
'''

import math
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class treeNode:
    def __init__(self,nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode
        self.children = {}

    def inc(self,numOccure):
        self.count += numOccure

    def disp(self,ind=1):
        for child in self.children.values():
            child.disp(ind+1)

def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat

def createInitSet( dataSet ):
    retdict = {}
    for trans in dataSet:
        retdict[ frozenset(trans) ] = 1
    return retdict

def createTree( dataSet, minSup=1 ):
    headerTable = {}
    for trans in dataSet:
        for item in trans:
            headerTable[item] = headerTable.get( item,0 ) + dataSet[trans]
    for k in headerTable.keys():
        if headerTable[k] < minSup:
            # del headerTable[k]
            del(headerTable[k])
    freqItemSet = set( headerTable.keys() )
    if len(freqItemSet) == 0:
        return None, None
    for k in headerTable.keys():
        headerTable[k] = [headerTable[k], None]
    retTree = treeNode( 'Null Set',1, None )
    for tranSet, count in dataSet.items():
        localD = {}
        for item in tranSet:
            if item in freqItemSet:
                localD[ item ] = headerTable[item][0]
        if len(localD) > 0:
            sortedLocalD = sorted( localD.items(),key=lambda x:x[1], reverse=True )
            orderedItems = [ v[0] for c in sortedLocalD ]
            updateTree(orderedItems, retTree, headerTable, count)
    return rettree, headerTable

def updateTree( items, inTree, headerTable, count ):
    if item[0] in inTree.children():
        inTree.children[items].inc(count)
    else:
        inTree.children[items] = treeNode(items[0],count,inTree)
        if headerTable[items[0]][1] = None:
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[item[0]][1], inTree.children[items[0]])
    if len(items) > 1:
        updateTree(items[1:], inTree.children[items[0]], headerTable, count)

def updateHeader(nodeToTest, targetNode):
    while nodeToTest.nodeLink != None:
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode

