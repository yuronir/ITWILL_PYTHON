import random
from copy import copy, deepcopy

EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = "----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------"
NAMES = [' ', 'X', 'O']

#보드 출력
def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells)) # format : 내부 인자를 뒤에서 순서대로 받아서 입력하기 위한 함수

#빈 판
def emptystate():
    return [[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY]]

def gameover(state):
    #가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
    for i in range(3):
        if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2]:
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:
            return state[0][i]
    #좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        return state[0][2]
    #판에 빈 칸이 남았는지
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                return EMPTY
    #판에 더 이상 빈 칸도 없고, 이긴 사람도 없다면 무승부
    return DRAW

# PLAYER_X가 선수(알 갯수가 같으면 마지막에 둔 것이 O, X가 하나 많으면 X)
def last_to_act(state):
    countx = 0
    counto = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == PLAYER_X:
                countx += 1
            elif state[i][j] == PLAYER_O:
                counto += 1
    if countx == counto:
        return PLAYER_O
    if countx == (counto + 1):
        return PLAYER_X
    return -1

# AI
class Agent(object):
    def __init__(self,player,verbose=False,lossval=0,learning=True):
        self.values = {}
        self.player = player
        self.verbose = verbose
        self.lossval = lossval
        self.learning = learning
        self.epsilon = 0.1
        self.alpha = 0.99
        self.prevstate = None
        self.prevscore =0
        self.count = 0

    def episode_over(self,winner):
        self.backup(self.winnerval(winner))
        self.prevstate = None
        self.prevscore = 0

    def action(self,state):
        r = random.random()
        if r < self.epsilon:
            move = self.random(state)
            self.log('>>>>>> Exploratory action: ' + str(move))
        else:
            move = self.greedy(state)
            self.log('>>>>>> Best action: ' + str(move))
        state[move[0]][move[1]] = self.player
        self.prevstate = self.statetuple(state)
        self.prevscore = self.lookup(state)
        return move

    def random(self,state):
        available = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == EMPTY:
                    available.append((i,j))
        return random.choice(available)

    def greedy(self,state):
        maxval = -50000
        maxmove = None
        if self.verbose:
            cells = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == EMPTY:
                    state[i][j] = self.player
                    val = self.lookup(state)
                    state[i][j] = EMPTY
                    if val > maxval:
                        maxval = val
                        maxmove = (i,j)
                    if self.verbose:
                        cells.append('{0:.3f}'.format(val).center(6))
                elif self.verbose:
                    cells.append(NAMES[state[i][j]].center(6))
        if self.verbose:
            print(BOARD_FORMAT.format(*cells))
        self.backup(maxval)
        return maxmove

    def backup(self,nextval):
        if self.prevstate != None and self.learning:
            self.values[self.prevstate] += self.alpha * (nextval - self.prevscore)

    def lookup(self,state):
        key = self.statetuple(state)
        if not key in self.values:
            self.add(key)
        return self.values[key]

    def add(self,state):
        winner= gameover(state)
        tup = self.statetuple(state)
        self.values[tup] = self.winnerval(winner)

    def winnerval(self,winner):
        if winner == self.player:
            return 1
        elif winner == EMPTY:
            return 0.5
        elif winner == DRAW:
            return 0
        else:
            return self.lossval

    #state를 tuple화해서 반환(3*3 list ->3*3 tuple)
    def statetuple(self,state):
        return (tuple(state[0]),tuple(state[1]),tuple(state[2]))

    def log(self,s):
        if self.verbose:
            print(s)

class Human(object):
    def __init__(self,player):
        self.player = player

    def action(self, state):
        printboard(state)
        action = None
        while action not in range(1,10):
            action = int(input('Your move? '))
        switch_map = {
            1: (0,0),
            2: (0,1),
            3: (0,2),
            4: (1,0),
            5: (1,1),
            6: (1,2),
            7: (2,0),
            8: (2,1),
            9: (2,2)
        }
        return switch_map[action]

    def episode_over(self,winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))

def play(agent1, agent2):
    state = emptystate()
    for i in range(9):
        if i % 2 == 0:
            move = agent1.action(state)
        else:
            move = agent2.action(state)
        state[move[0]][move[1]] = (i % 2) + 1
        winner = gameover(state)
        if winner != EMPTY:
            return winner
    return winner

if __name__ == "__main__":
    p1 = Agent(1, lossval=-1)
    p2 = Agent(2, lossval=-1)

    for i in range(10000):
        if i % 10 == 0:
            print('Game: {0}'.format(i))

        winner = play(p1,p2)
        p1.episode_over(winner)
        p2.episode_over(winner)

    while True:
        p2.verbose = True
        p1 = Human(1)
        winner = play(p1,p2)
        p1.episode_over(winner)
        p2.episode_over(winner)