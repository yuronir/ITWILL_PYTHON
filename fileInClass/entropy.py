
import math               # 엔트로피 계산에 로그함수를 쓰기 위해 math 모듈을 불러온다.

import collections


from collections import defaultdict

def class_probabilities(labels):       # 엔트로피 계산에 사용하는 컬럼의 확률을 계산하는 함수
    total_count = len(labels)
    return [count / total_count for count in collections.Counter(labels).values()]


def entropy(class_probabilities):
    return sum(-p * math.log(p, 2) for p in class_probabilities )


inputs = [
         ( {'cust_name':'SCOTT', 'card_yn':'Y', 'review_yn':'Y', 'before_buy_yn':'Y'}, True),
         ( {'cust_name':'SMITH', 'card_yn':'Y', 'review_yn':'Y', 'before_buy_yn':'Y'}, True),
         ( {'cust_name':'ALLEN', 'card_yn':'N', 'review_yn':'N', 'before_buy_yn':'Y'}, False),
         ( {'cust_name':'JONES', 'card_yn':'Y', 'review_yn':'N', 'before_buy_yn':'N'}, True),
         ( {'cust_name':'WARD',  'card_yn':'Y', 'review_yn':'Y', 'before_buy_yn':'Y'}, True) ]




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


for key in ['card_yn','review_yn','before_buy_yn']:
    print(partition_by(inputs, key).values())
    print(key,partition_entropy( partition_by(inputs,key).values()))