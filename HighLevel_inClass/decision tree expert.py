# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:58:56 2017

@author: stu
"""


#http://clearpal7.blogspot.kr/2016/07/3_10.html 
#http://yujuwon.tistory.com/entry/%EC%9D%98%EC%82%AC-%EA%B2%B0%EC%A0%95-%ED%8A%B8%EB%A6%AC

import operator
from math import log

def createDataSet():
     dataSet=[['M','30','NO','YES','NO','NO'],
                ['F','20','YES','YES','YES','NO'],
                ['F','20','YES','YES','NO','NO'],
                ['F','40','NO','NO','NO','NO'],
                ['F','30','NO','YES','NO','NO'],
                ['F','30','NO','NO','YES','NO'],
                ['F','20','NO','YES','NO','NO'],
                ['F','20','NO','YES','YES','YES'],
                ['F','30','YES','YES','NO','YES'],
                ['M','40','YES','NO','YES','NO'],
                ['M','20','NO','NO','NO','NO'],
                ['M','30','NO','YES','YES','NO'],
                ['M','20','YES','NO','NO','NO'],
                ['F','30','YES','YES','NO','YES'],
                ['M','30','YES','YES','YES','YES'],
                ['F','30','YES','NO','NO','NO'],
                ['F','30','NO','YES','YES','YES'],
                ['M','20','YES','YES','NO','NO'],
                ['M','40','YES','NO','YES','NO'],
                ['M','30','NO','NO','NO','NO'],
                ['F','30','YES','YES','NO','YES'],
                ['M','30','YES','NO','YES','NO'],
                ['F','40','NO','YES','YES','YES'],
                ['M','30','NO','YES','NO','NO'],
                ['F','30','YES','YES','YES','YES'],
                ['F','40','YES','NO','YES','NO'],
                ['M','40','YES','YES','NO','YES'],
                ['F','40','YES','YES','NO','YES']]
     
     labels=['GENDER','AGE','JOB_YN','MARRY_YN','CAR_YN','COUPON_YN']
     return dataSet, labels

def calcShannonEnt(dataSet):                #분할 전 엔트로피 구하기
    numEntries = len(dataSet)               #row의 개수 5
    labelCounts = {}
    for feaVec in dataSet:
        currentLabel = feaVec[-1]
        if currentLabel not in labelCounts:
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1      #labelCounts={'yes':2,'no':3}
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries 
        shannonEnt -= prob * log(prob, 2)   #yes:0.52877, no:0.97095
    return shannonEnt

def splitDataSet(dataSet, axis, value): #각 row에서 해당 변수제외하고 나머지 값들의 리스트
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
    
def chooseBestFeatureToSplit(dataSet):     #어떤 속성이 정보이득이 가장큰지
    numFeatures = len(dataSet[0]) - 1      #한 row가 갖는 속성의 개수-1
    baseEntropy = calcShannonEnt(dataSet)  #분할 전 엔트로피
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):           #dataSet의 target변수 제외 속성 리스트
        #[1, 1, 1, 0, 0] [1, 1, 0, 1, 1]
        featList = [example[i] for example in dataSet] 
        uniqueVals = set(featList)         #set() : 중복제거된 요소들 {0, 1}
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet) #분할 후 엔트로피
        infoGain = baseEntropy -newEntropy #정보이득
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature                     #가장 큰 정보이득을 갖는 속성
            

def majorityCnt(classList):     #가장 많은 빈도수의 값을 리턴해줌
    classCount = {}
    for vote in classList:      #['yes','yes','no','no','no']
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1   #classCount={'yes':2,'no':3}
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]    

    
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet] #['yes','yes','no','no','no']
    #종료조건1 : 모두 'yes'이거나 모두 'no'이면 종료하고 그 항목 리턴
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    #종료조건2 : [1,0,'yes']->[1,0]->[1] 데이터셋의 변수가 1개가 됐을 때 majorityCnt리턴
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)     #어떤 속성이 정보이득이 가장 큰지
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, 
                                        bestFeat, value),subLabels)
    return myTree
    
import matplotlib.pyplot as plt
decisionNode=dict(boxstyle="sawtooth", fc="0.8")
leafNode=dict(boxstyle="round4", fc="0.8")
arrow_args=dict(arrowstyle="<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
     createPlot.ax1.annotate(nodeTxt, xy=parentPt,
                                   xycoords='axes fraction',
                                   xytext=centerPt, textcoords='axes fraction',
                                   va="center", ha="ceneter", bbox=nodeType,
                                   arrowprops=arrow_args)

def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses 
    plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()


def getNumLeafs(myTree):
     numLeafs=0
     firstStr=myTree.keys()[0]
     secondDict=myTree[firstStr]
     for key in secondDict.keys():
          if type(secondDict[key]).__name__=='dict':
             numLeafs+=getNumLeafs(secondDict[key])
          else: numLeafs+=1
     return numLeafs
 
def getTreeDepth(myTree):
    maxDepth=0
    firstStr=myTree.keys()[0]
    secondDict=myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
           thisDepth=1+getTreeDepth(secondDict[key])
        else: thisDepth=1
        if thisDepth > maxDepth : maxDepth=thisDepth
    return maxDepth   

def classify(inputTree,featLabels,testVec):#괄호로 묶인 트리, 속성이름, 답
    firstStr=list(inputTree.keys())[0]
    secondDict=inputTree[firstStr]
    featIndex=featLabels.index(firstStr) #색인을 위한 분류 항목 표시 문자열 변환
    for key in secondDict.keys():
        if testVec[featIndex]==key:
           if type(secondDict[key]).__name__=='dict':
              classLabel=classify(secondDict[key], featLabels, testVec)
           else: classLabel=secondDict[key]
    return classLabel

def main():
    data,label = createDataSet()
    myTree = createTree(data,label)
    labels=['GENDER','AGE','JOB_YN','MARRY_YN','CAR_YN']
    a=[]
    for i in labels:
           a.append(input('{0}?'.format(i)).upper())
    answer=classify(myTree,labels,a)
    print('\n'+'쿠폰 반응여부 : '+answer)


if __name__=='__main__':
    main()
