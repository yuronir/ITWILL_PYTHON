'''
1.1) 시퀀스를 개별 변수로 나누기
'''
data = ['ACME', 50, 91.1, (2012, 12, 21)]

#모든 변수 담기
name, shares, price, date = data
print(date) #(2012, 12, 21)

#특정 값 무시하는 방법
_, shares, price, _ = data
print(shares) #50