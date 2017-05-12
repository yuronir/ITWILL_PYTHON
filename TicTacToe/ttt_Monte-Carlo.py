import random

# deepcopy : 메모리를 완전히 새롭게 생성
# copy : 껍데기만 카피, 내용은 동일한 곳을 가리킴

EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = "----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------"
NAMES = [' ', 'X', 'O']


# 보드 출력
def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells))


# 빈 판
def emptystate():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

def gameover(state):
    # 가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
    for i in range(3):
        if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2]:
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:
            return state[0][i]
    # 좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        return state[0][2]
    # 판이 비었는지
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                return EMPTY
    return DRAW

def randomGo(state):
    # 빈 칸 리스트업
    available = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                available.append((i, j))
    # 빈 칸 중에 선택하여 리턴
    return random.choice(available)


# play data 저장
class Agent(object):
    def __init__(self, player, verbose=False, lossval=0, learning=True):
        self.player = player  # 플레이어 넘버
        self.firstmove = None
        self.wincount = [0,0,0,0,0,0,0,0,0]
        self.losecount = [0,0,0,0,0,0,0,0,0]
        self.drawcount = [0,0,0,0,0,0,0,0,0]
        self.gamecount = [0,0,0,0,0,0,0,0,0]

    # 게임 종료 시 backup 함수로 피드백, state/score 리셋
    def episode_over(self, winner):
        self.updatecount(winner)
        self.firstmove = None

    def updatecount(self,winner):
        self.gamecount[self.firstmove[0] * 3 + self.firstmove[1]] += 1
        if winner == self.player:
            self.wincount[self.firstmove[0]*3+self.firstmove[1]] += 1
        elif winner == DRAW:
            self.drawcount[self.firstmove[0]*3+self.firstmove[1]] += 1
        else:
            self.losecount[self.firstmove[0]*3+self.firstmove[1]] += 1

    def setfirstmove(self,move):
        self.firstmove = move

    def printRate(self):
        for i in range(3):
            for j in range(3):
                winrate = self.wincount[3*i+j] / self.gamecount[3*i+j]
                print(winrate, end=" ")
            print('\n')

def play(p):
    state = emptystate()
    i = 0
    while(gameover(state) == EMPTY):
        move = randomGo(state)
        if i == 0:
            p.setfirstmove(move)
        state[move[0]][move[1]] = (i % 2) + 1
        i += 1
    return gameover(state)

if __name__ == "__main__":
    p = Agent(1)
    for i in range(100000):
        if i % 1000 == 0:
            print('Game: {0}'.format(i))

        winner = play(p)
        p.episode_over(winner)

    p.printRate()
