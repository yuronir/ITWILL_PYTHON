import math               # 엔트로피 계산에 로그함수를 쓰기 위해 math 모듈을 불러온다.
import collections
from collections import defaultdict

def getInputs():
    dataSet = [['M', '30', 'NO', 'YES', 'NO', 'NO'],
               ['F', '20', 'YES', 'YES', 'YES', 'NO'],
               ['F', '20', 'YES', 'YES', 'NO', 'NO'],
               ['F', '40', 'NO', 'NO', 'NO', 'NO'],
               ['F', '30', 'NO', 'YES', 'NO', 'NO'],
               ['F', '30', 'NO', 'NO', 'YES', 'NO'],
               ['F', '20', 'NO', 'YES', 'NO', 'NO'],
               ['F', '20', 'NO', 'YES', 'YES', 'YES'],
               ['F', '30', 'YES', 'YES', 'NO', 'YES'],
               ['M', '40', 'YES', 'NO', 'YES', 'NO'],
               ['M', '20', 'NO', 'NO', 'NO', 'NO'],
               ['M', '30', 'NO', 'YES', 'YES', 'NO'],
               ['M', '20', 'YES', 'NO', 'NO', 'NO'],
               ['F', '30', 'YES', 'YES', 'NO', 'YES'],
               ['M', '30', 'YES', 'YES', 'YES', 'YES'],
               ['F', '30', 'YES', 'NO', 'NO', 'NO'],
               ['F', '30', 'NO', 'YES', 'YES', 'YES'],
               ['M', '20', 'YES', 'YES', 'NO', 'NO'],
               ['M', '40', 'YES', 'NO', 'YES', 'NO'],
               ['M', '30', 'NO', 'NO', 'NO', 'NO'],
               ['F', '30', 'YES', 'YES', 'NO', 'YES'],
               ['M', '30', 'YES', 'NO', 'YES', 'NO'],
               ['F', '40', 'NO', 'YES', 'YES', 'YES'],
               ['M', '30', 'NO', 'YES', 'NO', 'NO'],
               ['F', '30', 'YES', 'YES', 'YES', 'YES'],
               ['F', '40', 'YES', 'NO', 'YES', 'NO'],
               ['M', '40', 'YES', 'YES', 'NO', 'YES'],
               ['F', '40', 'YES', 'YES', 'NO', 'YES']]

    labels = ['GENDER', 'AGE', 'JOB_YN', 'MARRY_YN', 'CAR_YN', 'COUPON_YN']

    res = []
    for data in dataSet:
        temp = {}
        for i in range(len(data)-1):
            temp[labels[i]] = data[i]
        res.append((temp,True if data[5] == 'YES' else False))
    return res


def class_probabilities(labels):       # 엔트로피 계산에 사용하는 컬럼의 확률을 계산하는 함수
    total_count = len(labels)
    return [count / total_count for count in collections.Counter(labels).values()]


def entropy(class_probabilities):
    return sum(-p * math.log(p, 2) for p in class_probabilities )


def partition_by(inputs, attribute):
    groups = defaultdict(list)
    for input in inputs:
        key=input[0][attribute]
        groups[key].append(input)
    return groups


def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    # print('labels : ', labels)
    probabilities = class_probabilities(labels)
    # print ('entropy(probabilities : ' ,entropy(probabilities))
    return entropy(probabilities)


def partition_entropy(subsets):         # 파티션된 노드들의 엔트로피
    total_count = sum(len(subset) for subset in subsets)        # subset은 라벨이 있는 데이터의 리스트의 리스트이다. 이것에 대한 엔트로피를 계산한다.
    # for subset in subsets:
    #     print('subset : ', subset)
    #     print('len(subset) : ', len(subset))
    #     print('data_entropy(subset) : ', data_entropy(subset))
    return sum(data_entropy(subset) * len(subset) / total_count for subset in subsets)


inputs = getInputs()
print(inputs)
for key in inputs[0][0].keys():
    # print(partition_by(inputs, key).values())
    print(key,partition_entropy( partition_by(inputs,key).values()))