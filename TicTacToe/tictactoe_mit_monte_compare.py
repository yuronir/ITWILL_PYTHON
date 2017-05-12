import random
from copy import copy, deepcopy

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


# PLAYER_X가 선수 (알이 하나 더 많으면 마지막에 둔 것)
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


# values 초기값 입력 (제대로 작동 안 하는듯? 하다가 맘)
def enumstates(state, idx, agent):
    if idx > 8:
        player = last_to_act(state)
        if player == agent.player:
            agent.add(state)
    else:
        winner = gameover(state)
        if winner != EMPTY: #승패가 결정났을때
            return
        i = int(idx / 3)
        j = idx % 3
        for val in range(3):
            state[i][j] = val
            enumstates(state, idx + 1, agent)


# AI
class Agent(object):
    def __init__(self, player, epsilon=0.1, verbose=False, lossval=0, learning=True):
        self.values = {}
        self.player = player  # 플레이어 넘버
        self.verbose = verbose  # 상세 출력모드(true일 시 콘솔에 막 찍음)
        self.lossval = lossval
        self.learning = learning  # 셀프 러닝 모드
        self.epsilon = epsilon  # 랜덤수 착수 비율
        self.alpha = 0.99   # 영향 감소 계수(승패결정수에서 되감기할수록 영향력이 떨어짐)
        self.prevstate = None
        self.prevscore = 0
        self.count = 0
        #enumstates(emptystate(), 0, self)

    # 게임 종료 시 backup 함수로 피드백, state/score 리셋
    def episode_over(self, winner):
        self.backup(self.winnerval(winner))
        self.prevstate = None
        self.prevscore = 0

    def action(self, state):
        r = random.random()
        # random의 결과가 epsilon(0.1) 아래일 시(10% 확률) 새로운 길(랜덤) 도전 !
        if r < self.epsilon:
            move = self.random(state)
            self.log('>>>>>>> Exploratory action: ' + str(move))
        # 90% 확률로 스스로의 학습 결과로 가진 최선수 착수 !
        else:
            move = self.greedy(state)
            self.log('>>>>>>> Best action: ' + str(move))
        state[move[0]][move[1]] = self.player
        self.prevstate = self.statetuple(state)
        self.prevscore = self.lookup(state)
        state[move[0]][move[1]] = EMPTY
        return move

    # 착수 위치 임의로 선택 기능
    def random(self, state):
        # 빈 칸 리스트업
        available = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == EMPTY:
                    available.append((i, j))
        # 빈 칸 중에 선택하여 리턴
        return random.choice(available)

    # 현재 지닌 정보를 바탕으로 최선수 선택
    def greedy(self, state):
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
                        maxmove = (i, j)
                    if self.verbose:
                        cells.append('{0:.3f}'.format(val).center(6))
                elif self.verbose:
                    cells.append(NAMES[state[i][j]].center(6))
        if self.verbose:
            print(BOARD_FORMAT.format(*cells))
        self.backup(maxval)
        return maxmove

    # 매 수마다 머신러닝
    # 다음 수의 정보들 중 최선수를 찾아 선택하고, 현재의 판에 대해 해당 최선수의 rate를 가산점으로 반영
    def backup(self, nextval):
        if self.prevstate != None and self.learning:
            self.values[self.prevstate] += self.alpha * (nextval - self.prevscore)

    # 해당 state의 value 반환(없으면 add함수를 통해 새로 생성하여 반환)
    def lookup(self, state):
        key = self.statetuple(state)
        if not key in self.values:
            self.add(key)
        return self.values[key]

    # values에 넣기 위한 state tuple 생성(value는 gameover/winnerval을 통해 결정)
    def add(self, state):
        winner = gameover(state)
        tup = self.statetuple(state)
        self.values[tup] = self.winnerval(winner)

    # 승패/미종료 시 각각에 해당하는 value 반환
    def winnerval(self, winner):
        if winner == self.player:
            return 1
        elif winner == EMPTY:
            return 0.5
        elif winner == DRAW:
            return 0
        else:
            return self.lossval

    def printvalues(self):
        vals = deepcopy(self.values)
        for key in vals:
            state = [list(key[0]), list(key[1]), list(key[2])]
            cells = []
            for i in range(3):
                for j in range(3):
                    if state[i][j] == EMPTY:
                        state[i][j] = self.player
                        cells.append(str(self.lookup(state)).center(3))
                        state[i][j] = EMPTY
                    else:
                        cells.append(NAMES[state[i][j]].center(3))
            print(BOARD_FORMAT.format(*cells))

    # state를 tuple화해서 반환(3*3 list ->3*3 tuple)
    def statetuple(self, state):
        return (tuple(state[0]), tuple(state[1]), tuple(state[2]))

    # verbose가 on일때만 로그 찍히게
    def log(self, s):
        if self.verbose:
            print(s)


# 사람
class Human(object):
    def __init__(self, player):
        self.player = player

    # 착수
    def action(self, state):
        printboard(state)
        action = None
        while action not in range(1, 10):
            action = int(input('Your move? '))
        switch_map = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        return switch_map[action]

    def episode_over(self, winner):
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
    return winner # 지역변수를 더 바깥 범위에서도 쓸 수 있다니!?


if __name__ == "__main__":
    #20% 확률 랜덤수
    p1 = Agent(1, epsilon=0.2,lossval=-1)
    p2 = Agent(2, epsilon=0.2,lossval=-1)

    #랜덤수 없이
    p3 = Agent(1, epsilon=0, lossval=-1)
    p4 = Agent(2, epsilon=0, lossval=-1)

    #각각 학습
    for i in range(30000):
        if i % 1000 == 0:
            print('Game: {0}'.format(i))

        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)

        winner = play(p3, p4)
        p3.episode_over(winner)
        p4.episode_over(winner)

    print('Learning Finished!')
    print('Battle Start!')

    #p1 vs p4, p3 vs p2로 승률 비교
    p1.epsilon=0.1
    p2.epsilon=0.1
    p3.epsilon=0.1
    p4.epsilon=0.1
    '''
    p1.learning = False
    p2.learning = False
    p3.learning = False
    p4.learning = False
    '''
    # p1 승리횟수, p4 승리횟수, 무승부 횟수
    p1p4_wincount = [0, 0, 0]
    p2p3_wincount = [0, 0, 0]
    battlecount = 50000
    for i in range(battlecount):
        '''
        p1 : 선수 랜덤수O
        p2 : 후수 랜덤수O
        p3 : 선수 랜덤수X
        p4 : 후수 랜덤수X
        '''
        if i % 1000 == 0:
            print('Game: {0}'.format(i))
        winner = play(p1, p4)
        if winner == 1:
            p1p4_wincount[0] += 1
        elif winner == 2:
            p1p4_wincount[1] += 1
        elif winner == DRAW:
            p1p4_wincount[2] += 1

        winner = play(p3, p2)
        if winner == 1:
            p2p3_wincount[1] += 1
        elif winner == 2:
            p2p3_wincount[0] += 1
        elif winner == DRAW:
            p2p3_wincount[2] += 1
    print('Battle End !\nWincount(P1 vs P4, P2 vs P3) : ')
    print('P1(MCTS 1st)''s Winrate : ', p1p4_wincount[0]/battlecount)
    print('P4(NoRandom 2nd)''s Winrate : ', p1p4_wincount[1] / battlecount)
    print('P2(MCTS 2nd)''s Winrate : ', p2p3_wincount[0]/battlecount)
    print('P3(NoRandom 1st)''s Winrate : ', p2p3_wincount[1]/battlecount)