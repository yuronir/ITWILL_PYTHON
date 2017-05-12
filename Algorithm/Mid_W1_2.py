file = open('D:\data\\algorithm_input\midQ2.txt','r')
inp = []

#string 형태의 숫자 두 개를 입력받아 strike 수 반환
def strikeCount(n1, n2):
    res = 0
    for i in range(len(n1)):
        if n1[i] == n2[i]:
            res += 1
    return res

#string 형태의 숫자 두개를 입력받아 ball 수 반환
def ballCount(n1, n2):
    res = 0
    for i in range(len(n1)):
        for j in range(len(n2)):
            if i != j and n1[i] == n2[j]:
                res += 1
    return res

#정답 리스트 초기화(모든 경우의 수)
ansList = []
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i != j and i != k and j != k:
                ansList.append(str(i) + str(j) + str(k))

#파일 리스트에 입력
for i in range(int(file.readline())):
    temp = file.readline().split(' ')
    inp.append([temp[0],int(temp[1]),int(temp[2])])

#각 질답에 대해 정답일 수 없는 조합 제거
#i 예시 : ['123',1,1]
for i in inp:
    delList = []
    for j in ansList:
        if strikeCount(i[0],j) != i[1] or ballCount(i[0],j) != i[2]:
            delList.append(j)
    for k in delList:
        ansList.remove(k)

print(ansList)
print(len(ansList))