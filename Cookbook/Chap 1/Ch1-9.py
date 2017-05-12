'''
1.9) 두 딕셔너리의 유사점 찾기
    두 딕셔너리의 유사점을 찾기 위해서는 keys()와 items() 메소드에 집합 연산을 수행한다.
    
keys() : 키를 노출하는 키-뷰 객체 반환
items() : (key,value) 페어로 구성된 아이템-뷰 객체 반환
&, -
'''

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

#동일한 키 찾기
res = a.keys() & b.keys()
print(res) # {'y', 'x'}

#a에만 있고 b에는 없는 키 찾기
res = a.keys() - b.keys()
print(res) # {'z'}

#키와 값이 모두 동일한 것 찾기
res = a.items() & b.items()
print(res) # {('y', 2)}

#특정 키를 제거한 새로운 딕셔너리 만들기
c = {key:a[key] for key in a.keys() - {'z','w'}}
print(c) # {'y': 2, 'x': 1}
