import random
from copy import deepcopy

Player_X = 1
Player_O = 2

class Tictactoe(object):
    def __init__(self):
        self.state = self.emptyBoard()
        self.EMPTY = 0
        self.DRAW = -1
        self.markEnum = (' ', 'X', 'O')
        self.stonecount = 0

    # ex) loc = (1,2)
    def putStone(self, player, loc):
        self.state[loc[0]][loc[1]] = player
        self.stonecount += 1

    #특정 위치가 비었는지 확인
    def isEmptyPoint(self,loc):
        if self.state[loc[0]][loc[1]] == self.EMPTY:
            return True
        return False

    #현재 착수된 돌 갯수 출력
    def getStoneCount(self):
        return self.stonecount

    #판 출력
    def printBoard(self):
        print('------------------------')
        for i in range(3):
            print('|', end='')
            for j in range(3):
                print('   {0}   |'.format(self.markEnum[self.state[i][j]]), end='')
            print('\n------------------------')

    #빈 판 반환
    def emptyBoard(self):
        return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    #빈 칸 리스트업
    def getEmptyPoints(self):
        res = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == self.EMPTY:
                    res.append([i,j])
        return res

    def checkBoard(self):
        # 가로 한줄 완성한 사람 승리 : 리턴
        # 세로 한줄 완성시 승리
        for i in range(3):
            if self.state[i][0] != self.EMPTY and self.state[i][0] == self.state[i][1] and self.state[i][0] == self.state[i][2]:
                return self.state[i][0]
            if self.state[0][i] != self.EMPTY and self.state[0][i] == self.state[1][i] and self.state[0][i] == self.state[2][i]:
                return self.state[0][i]

        # 대각선 완성시 승리
        if self.state[0][0] != self.EMPTY and self.state[0][0] == self.state[1][1] and self.state[0][0] == self.state[2][2]:
            return self.state[0][0]
        if self.state[0][2] != self.EMPTY and self.state[0][2] == self.state[1][1] and self.state[0][2] == self.state[2][0]:
            return self.state[0][2]

        # 판이 덜 찼으면 self.EMPTY 반환
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == self.EMPTY:
                    return self.EMPTY
        # 그 외 무승부
        return self.DRAW

    def playGame(self, p1, p2):
        while self.checkBoard() == self.EMPTY:
            self.printBoard()
            if self.getStoneCount()%2 == 0:
                self.putStone(Player_X, p1.decide(self))
            else:
                self.putStone(Player_O, p2.decide(self))
        return self.checkBoard()

class Human(object):
    def __init__(self,pnum):
        self.pnum = pnum
        
    def decide(self,board):
        inp = int(input('Where do you want? '))
        res = self.conversion(inp)
        if board.isEmptyPoint(res):
            return res
        else:
            print("Wrong Point ! ")
            return self.decide(board)
        
    def conversion(self,inp):
        point = [[999, 999],
                 [0, 0],
                 [0, 1],
                 [0, 2],
                 [1, 0],
                 [1, 1],
                 [1, 2],
                 [2, 0],
                 [2, 1],
                 [2, 2]]
        return point[inp]

    def gameover(self,winner):
        if winner == self.pnum:
            print("You Win !".format(winner))
        else:
            print("You Lose !")

class AI(object):
    def __init__(self,pnum):
        self.pnum = pnum
        self.alpha = 0.99
        self.mcts = 0.1
        self.learning = True
        self.values = {}
        self.prevstate = None

    # 게임 종료시 기록
    def gameover(self):
        print('end!')

    def decide(self,board):
        r = random.random()
        if r < self.mcts:
            loc = self.randomDecide(board)
        else: #greedy
            loc = self.greedyDecide(board)
        self.prevstate[loc[0],loc[1]] = self.pnum
        return loc

    def randomDecide(self,board):
        eplist = board.getEmptyPoints()
        r = random.randint(0,len(eplist))
        return eplist[r]

    def greedyDecide(self,board):
        maxVal = -10000
        maxLoc = None
        emptyPointList = board.getEmptyPoints()
        for loc in emptyPointList:
            board.state[loc[0]][loc[1]] = self.pnum
            key = self.stateTuple(board.state)
            if key not in self.values:
                self.addValue(board)
            board.state[loc[0]][loc[1]] = board.EMPTY
            if maxVal < self.values(board.state):
                maxVal = self.values(board.state)
                maxLoc = loc
        self.feedback(maxVal)
        return maxLoc

    def feedback(self,nextVal):
        if self.learning == True:
            self.values[self.prevstate] += self.alpha * (nextVal - self.values[self.prevstate])

    def addValue(self,board):
        res = board.checkBoard()
        stateTup = self.stateTuple(board.state)
        self.values[stateTup] = self.winnerVal(res,board)

    def winnerVal(self,result,board):
        if result == self.pnum:
            return 1
        elif result == board.EMPTY:
            return 0.5
        elif result == board.DRAW:
            return 0
        else:
            return -1

    def stateTuple(self,state):
        return (tuple(state[0]),tuple(state[1]),tuple(state[2]))


if __name__ == "__main__":
    p1 = AI(1)
    p2 = Human(2)
    board = Tictactoe()
    winner = board.playGame(p1,p2)
    p1.gameover(winner)
    p2.gameover(winner)