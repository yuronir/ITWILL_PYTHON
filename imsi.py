from math import log
import collections

# 각 데이터의 확률을 받아서 엔트로피 계산
def entropy(pset):
    return sum((-p * log(p, 2) for p in pset))

# 항목별 각 데이터의 비율 반환
def class_probabilities(labels):
    return [p/len(labels) for p in collections.Counter(labels).values()]


## 기존의 사람별 데이터를 항목별 집계값으로 재구성
def restruct_data(inputs):
    res = {}
    for key in inputs[0][0].keys():
        res[key] = [x[0][key] for x in inputs]
    return res

##
def column_data(inputs, column):
    groups = defaultdict(list)
    for input in inputs:
        key = input[0][column]
        groups[key].append(input[1])
    return dict(groups)

## 전체 데이터들에 대한 분할 전 엔트로피값 반환
def get_entropy_before_split(inputs):
    for key in ['card_yn', 'review_yn', 'before_buy_yn']:
        p = class_probabilities(inputs[key])
        print('{0} : {1}'.format(key, entropy(p)))


## 준호 코드. 아직 미연결
def partition_entropy(subsets):         # 파티션된 노드들의 엔트로피
    total_count = sum(len(subset) for subset in subsets)        # subset은 라벨이 있는 데이터의 리스트의 리스트이다. 이것에 대한 엔트로피를 계산한다.
    return sum(get_entropy_before_split(subset) * len(subset) / total_count for subset in subsets)


## 전체 데이터들에 대한 분할 후 엔트로피값 반환 (미완성)
def get_entropy_after_split(inputs):
    groups = {}
    for key in ['card_yn', 'review_yn', 'before_buy_yn']:
        groups[key] = column_data(inputs, key)
    print(groups)
    for k in groups.keys():
        for key in groups[k].keys():
            print(k, partition_entropy(groups[k][key]))

inputs = [
         ( {'cust_name':'SCOTT', 'card_yn':'Y', 'review_yn':'Y', 'before_buy_yn':'Y'}, True),
         ( {'cust_name':'SMITH', 'card_yn':'Y', 'review_yn':'Y', 'before_buy_yn':'Y'}, True),
         ( {'cust_name':'ALLEN', 'card_yn':'N', 'review_yn':'N', 'before_buy_yn':'Y'}, False),
         ( {'cust_name':'JONES', 'card_yn':'Y', 'review_yn':'N', 'before_buy_yn':'N'}, True),
         ( {'cust_name':'WARD',  'card_yn':'Y', 'review_yn':'Y', 'before_buy_yn':'Y'}, True) ]


data = restruct_data(inputs)
# get_entropy_before_split(data)


from collections import defaultdict
group1 = {}
group1['one'] = 'a'

group2 = defaultdict(lambda :'a')
group2['one']   # {'one': 'a'}

group3 = defaultdict(list)
group3['one']   # {'one': []}
print(data)
print(column_data(inputs, 'review_yn'))
get_entropy_after_split(inputs)