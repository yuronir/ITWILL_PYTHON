import threading
import matplotlib.pyplot as plt
import math
import random

class Messenger(threading.Thread):
    def run(self):
        for _ in range(50):
            print(threading.currentThread().getName())

circle = plt.Circle((0, 0), radius=1.0, fc='w', ec='b')  # 원 만들기
# 원의 중심이(0,0) 이고 반지름이 1이다. 채워짐색: white 테두리색: black
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))  # x축 범위 (-1.1) y축 범위(-1,1)
ax.set_aspect('equal')  # 가로 세로축이 같은 스케일이 되도록 크기 조정
plt.gca().add_patch(circle)  # 원 그리기
dot_cnt = 1000  # dot_cnt가  100000일 때와 1000000일 때를 비교
cnt_in = 0

for i in range(dot_cnt):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    plt.plot([x], [y], 'ro')  # 랜덤 점 찍기
    if math.pow(x, 2) + math.pow(y, 2) <= 1:
        cnt_in += 1

plt.show()
print('원의 넓이 : ')
print((cnt_in / dot_cnt) * 4)

# send = Messenger(name='Sending out messages')
# receive = Messenger(name='Receiving messages')
#
# send.start()
# receive.start()

