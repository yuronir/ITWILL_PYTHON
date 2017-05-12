import operator
from math import log
import time


def createdataset():
    dataset = [['남', '30대', 'no', 'yes', 'no', 'no'],
               ['여', '20대', 'yes', 'yes', 'yes', 'no'],
               ['여', '20대', 'yes', 'yes', 'no', 'no'],
               ['여', '40대', 'no', 'no', 'no', 'no'],
               ['여', '30대', 'no', 'yes', 'no', 'no'],
               ['여', '30대', 'no', 'no', 'yes', 'no'],
               ['여', '20대', 'no', 'yes', 'no', 'no'],
               ['여', '20대', 'no', 'yes', 'yes', 'yes'],
               ['여', '30대', 'yes', 'yes', 'no', 'yes'],
               ['남', '40대', 'yes', 'no', 'yes', 'no'],
               ['남', '20대', 'no', 'no', 'no', 'no'],
               ['남', '30대', 'no', 'yes', 'yes', 'no'],
               ['남', '20대', 'yes', 'no', 'no', 'no'],
               ['여', '30대', 'yes', 'yes', 'no', 'yes'],
               ['남', '30대', 'yes', 'yes', 'yes', 'yes'],
               ['여', '30대', 'yes', 'no', 'no', 'no'],
               ['여', '30대', 'no', 'yes', 'yes', 'yes'],
               ['남', '20대', 'yes', 'yes', 'no', 'no'],
               ['남', '40대', 'yes', 'no', 'yes', 'no'],
               ['남', '30대', 'no', 'no', 'no', 'no'],
               ['여', '30대', 'yes', 'yes', 'no', 'yes'],
               ['남', '30대', 'yes', 'no', 'yes', 'no'],
               ['여', '40대', 'no', 'yes', 'yes', 'yes'],
               ['남', '30대', 'no', 'yes', 'no', 'no'],
               ['여', '30대', 'yes', 'yes', 'yes', 'yes'],
               ['여', '40대', 'yes', 'no', 'yes', 'no'],
               ['남', '40대', 'yes', 'yes', 'no', 'yes'],
               ['여', '40대', 'yes', 'yes', 'no', 'yes']]
    labels = ['gender', 'age', 'job_yn', 'marry_yn', 'car_yn', 'coupon_yn']
    return dataset, labels


def calcshannonent(dataset):  # 분할 전 엔트로피 구하기
    numentries = len(dataset)  # row의 개수 5
    labelcounts = {}
    for feavec in dataset:
        currentlabel = feavec[-1]
        if currentlabel not in labelcounts:
            labelcounts[currentlabel] = 0
        labelcounts[currentlabel] += 1  # labelcounts={'yes':2,'no':3}
    shannonent = 0.0
    for key in labelcounts:
        prob = float(labelcounts[key]) / numentries
        shannonent -= prob * log(prob, 2)  # yes:0.52877, no:0.97095
    return shannonent


def splitdataset(dataset, axis, value):  # 각 row에서 해당 변수제외하고 나머지 값들의 리스트
    retdataset = []
    for featvec in dataset:
        if featvec[axis] == value:
            reducedfeatvec = featvec[:axis]
            reducedfeatvec.extend(featvec[axis + 1:])
            retdataset.append(reducedfeatvec)
    return retdataset


def choosebestfeaturetosplit(dataset):  # 어떤 속성이 정보이득이 가장큰지
    numfeatures = len(dataset[0]) - 1  # 한 row가 갖는 속성의 개수-1
    baseentropy = calcshannonent(dataset)  # 분할 전 엔트로피
    bestinfogain = 0.0
    bestfeature = -1
    for i in range(numfeatures):  # dataset의 target변수 제외 속성 리스트
        # [1, 1, 1, 0, 0] [1, 1, 0, 1, 1]
        featlist = [example[i] for example in dataset]
        uniquevals = set(featlist)  # set() : 중복제거된 요소들 {0, 1}
        newentropy = 0.0
        for value in uniquevals:
            subdataset = splitdataset(dataset, i, value)
            prob = len(subdataset) / float(len(dataset))
            newentropy += prob * calcshannonent(subdataset)  # 분할 후 엔트로피
        infogain = baseentropy - newentropy  # 정보이득
        if infogain > bestinfogain:
            bestinfogain = infogain
            bestfeature = i
    return bestfeature  # 가장 큰 정보이득을 갖는 속성


def majoritycnt(classlist):  # 가장 많은 빈도수의 값을 리턴해줌
    classcount = {}
    for vote in classlist:  # ['yes','yes','no','no','no']
        if vote not in classcount.keys():
            classcount[vote] = 0
        classcount[vote] += 1  # classcount={'yes':2,'no':3}
    sortedclasscount = sorted(classcount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedclasscount[0][0]


def createtree(dataset, labels):
    classlist = [example[-1] for example in dataset]  # ['yes','yes','no','no','no']
    # 종료조건1 : 모두 'yes'이거나 모두 'no'이면 종료하고 그 항목 리턴
    if classlist.count(classlist[0]) == len(classlist):
        return classlist[0]
    # 종료조건2 : [1,0,'yes']->[1,0]->[1] 데이터셋의 변수가 1개가 됐을 때 majoritycnt리턴
    if len(dataset[0]) == 1:
        return majoritycnt(classlist)
    bestfeat = choosebestfeaturetosplit(dataset)  # 어떤 속성이 정보이득이 가장 큰지
    bestfeatlabel = labels[bestfeat]
    mytree = {bestfeatlabel: {}}
    del (labels[bestfeat])
    featvalues = [example[bestfeat] for example in dataset]
    uniquevals = set(featvalues)
    for value in uniquevals:
        sublabels = labels[:]
        mytree[bestfeatlabel][value] = createtree(splitdataset(dataset,
                                                               bestfeat, value), sublabels)
    return mytree


def main():
    data, label = createdataset()
    t1 = time.clock()
    mytree = createtree(data, label)
    t2 = time.clock()
    print(mytree)
    print('execute for ', t2 - t1)  # 실행시간 재는거


if __name__ == '__main__':
    main()