
word_list = []
cont_list = []
values = {}
for i in range(7): #단어 리스트 담기
    path = "D:\data\korean_word\word_0" + str(i) + ".txt"
    with open(path,'r') as file:
        for word in file:
            word_list.append(word)

for i in range(3): #문장 리스트 담기
    path = "D:\data\korean_word\cont_0" + str(i) + ".txt"
    with open(path,'r') as file:
        for content in file:
            cont_list.append(content)

idx = 0
while 1 == 1:
    for i in word_list:
        print()

    break;

