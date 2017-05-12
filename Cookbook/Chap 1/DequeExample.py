from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q) #deque([1, 2, 3], maxlen=3)

#최대 길이를 초과하면 가장 왼쪽 값을 밀어낸다
q.append(4)
print(q) #deque([2, 3, 4], maxlen=3)

#왼쪽에 삽입
q.appendleft(10)
print(q) #deque([10, 2, 3], maxlen=3)

#오른쪽에 값을 삽입하면 다시 제일 왼쪽의 10이 밀려난다(삽입순서가 아님을 확인)
q.append(20)
print(q) #deque([2, 3, 20], maxlen=3)

