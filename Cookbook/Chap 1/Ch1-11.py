'''
1.11) 슬라이스 이름 붙이기
    슬라이스 하드코딩의 가독성을 높이기 위한 방안
    
slice() : 슬라이스 받는 모든 곳에 사용 가능
slice(start,stop,step)
'''

record = 'abcde동작구사당동'
ADDRESS = slice(5,11)
print(record[ADDRESS]) # 동작구사당동
a = slice(3,9,2)
print(record[a])