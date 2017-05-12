'''
1.6) 딕셔너리의 키를 여러 값에 매핑하기
    => value를 리스트 등의 컨테이너로 만든다. 

세트 : key로만 이루어진 유형.(key이므로 중복이 허용되지 않음)
defaultdict : 첫번째 값을 자동으로 초기화해주는 자료형(그래서 초기화하지 않고 append를 바로 쓰는 등이 가능)
'''

# 아이템의 삽입 순서를 지키고 싶다면 리스트를, 순서는 상관 없이 중복을 없애고 싶으면 세트를 사용
#리스트
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

#세트
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

##예제 1)
#defaultdict : 첫번째 값을 자동으로 초기화해주므로 사용자는 아이템 추가에만 집중할 수 있다.
#딕셔너리에 없는 값이라도 한 번이라도 접근한 키의 엔트리를 자동으로 생성한다는 점에 주의!
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1) # 'a'를 defaultdict에서 자동으로 초기화해줌
print(d) #defaultdict(<class 'list'>, {'a': [1]})

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d) #defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {4}})