import random

dot_cnt = int(input('점 갯수를 입력하세요 : '))
cnt_in = 0
for i in range(dot_cnt):
	x = random.uniform(-1,1)
	y = random.uniform(-1,1)
	if (x*x + y*y) < 1:
			cnt_in = cnt_in + 1
res = 4 * (cnt_in / dot_cnt)
print(dot_cnt)
print(cnt_in)
print(res)