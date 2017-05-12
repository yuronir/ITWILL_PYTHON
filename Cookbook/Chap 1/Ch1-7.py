'''
1.7) 딕셔너리 순서 유지

OrderedDIct : 삽입 초기의 순서를 그대로 기억.
    Doubly Linked List로, 삽입 순서와 관련된 키를 기억한다.
    기존 키에 재할당을 하더라도 순서에는 변화가 생기지 않는다.
    더블 링크드 리스트이기 때문에 일반적인 딕셔너리보다 2배 크다.
    따라서 크기가 매우 큰 데이터 구조체를 만든다면, 이 추가적인 메모리 소비가 애플리케이션에 실질적으로 유용한지 유심히 살펴보아야 한다.
'''
from collections import OrderedDict

#OrderedDict는 삽입 초기의 순서를 그대로 기억한다.
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# "foo 1" "bar 2" "spam 3" "grok 4"
for key in d:
    print(key,d[key])

# 나중에 직렬화하거나 다른 포맷으로 인코딩할 다른 매핑을 만들 때 특히 유용하다.
import json
json.dumps(d) #{"foo": 1, "bar": 2, "spam": 3, "grok": 4}
