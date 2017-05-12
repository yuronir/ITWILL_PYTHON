#러닝 타임을 중시한 버전(이중루프 1회 / 중간에 break 존재)
'''
파일 생성 코드
with open('D:\data\\algorithm_input\highQ1_100.txt','w') as file:
    file.write('100\n')
    for i in range(100):
        line = ''
        for j in range(100):
            line += str((i+j)%2) + ' '
        file.write(line.rstrip() + '\n')
'''
file = open('D:\data\\algorithm_input\highQ1_100.txt','r')
matrixSize = int(file.readline())
input = []
for i in range (matrixSize):
    input.append([int(x) for x in file.readline().split(' ')])

rowParity = 0 #nonParity cnt
colParity = 0 #nonParity cnt
rowPoint = -1 #Change bit rowaddr
colPoint = -1 #Change bit coladdr
result = 0 #0 : OK, 1 : Change bit, 2 : Corrupt

for i in range(matrixSize):
    tempRow = 0 #체크할 row에서의 1의 갯수
    tempCol = 0 #체크할 col에서의 1의 갯수
    for j in range(matrixSize):
        if input[i][j] == 1:
            tempRow += 1
        if input[j][i] == 1:
            tempCol += 1
    if tempRow%2 == 1:
        if rowParity == 1:
            result = 2
            break
        else:
            rowParity += 1
            rowPoint = i
    if tempCol%2 == 1:
        if colParity == 1:
            result = 2
            break
        else:
            colParity += 1
            colPoint = i

for i in input:
    print(i)

#col/row중 한쪽에만 홀수줄이 존재할 경우 or col이나 row에 2개 이상의 홀수줄이 존재할 경우 : Corrupt
if result == 2 or colParity+rowParity == 1:
    print('Corrupt')
#col/row에 하나씩의 홀수줄이 존재할 경우 : Change bit
elif colParity == 1 and rowParity == 1:
    print('Change bit ({0},{1})'.format(rowPoint+1,colPoint+1))
#그 외(홀수줄이 하나도 없는 경우) : OK
else:
    print('OK')