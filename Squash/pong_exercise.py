import pygame, sys
from pygame.locals import *

#Number of frames per second
#Change this value to speed up or slow down your game.
FPS = 200
INCREASESPEED = 5

#Global Variables to be used through our program
WINDOWWIDTH = 400
WINDOWHEIGHT = 300
LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 20

#Set up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#Set Direction Enum
LEFT = -1
RIGHT = 1
UP = -1
DOWN = 1

#Draws the arena the game will be played in.
def drawArena():
    DISPLAYSURF.fill((0,0,0))
    #Draw outline of arena
    pygame.draw.rect(DISPLAYSURF,WHITE,((0,0),(WINDOWWIDTH,WINDOWHEIGHT)),LINETHICKNESS*2)
    #Draw centre line
    pygame.draw.line(DISPLAYSURF,WHITE,(int(WINDOWWIDTH/2),0),(int(WINDOWWIDTH/2),WINDOWHEIGHT),int(LINETHICKNESS/4))

#Draws the paddle
def drawPaddle(paddle):
    #Stops paddle moving too low
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    #Stops paddle moving too high
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    #Draws paddle
    pygame.draw.rect(DISPLAYSURF,WHITE,paddle)

#Draws the ball
def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF,WHITE,ball)

#moves the ball returns new position
def moveBall(ball,ballDirX,ballDirY):
    ball.x += ballDirX * INCREASESPEED
    ball.y += ballDirY * INCREASESPEED
    return ball

#Checks for a collision  with a wall, and 'bounces' ball off it.
#Returns new direction
def checkEdgeCollision(ball, ballDirX, ballDirY):
    if ball.top == (LINETHICKNESS) or ball.bottom == (WINDOWHEIGHT - LINETHICKNESS):
        ballDirY *= -1
    if ball.left == (LINETHICKNESS) or ball.right == (WINDOWWIDTH - LINETHICKNESS):
        ballDirX *= -1
    return ballDirX, ballDirY

#Checks is the ball has hit a paddle, and 'bounces' ball off it.
def checkHitBall(ball, paddle1, paddle2, ballDirX):
    if ballDirX == LEFT and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
        return -1
    elif ballDirX == RIGHT and paddle2.left == ball.right and paddle2.top < ball.top and paddle2.bottom > ball.bottom:
        return -1
    else: return 1

#Checks to see if a point has been scored returns new score
def checkPointScored(paddle1, ball, score, ballDirX):
    #공을 놓쳤을 시 0점으로 리셋
    if ball.left == LINETHICKNESS:
        return 0
    #공을 칠 때마다 1점 추가
    elif ballDirX == LEFT and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
        score += 1
        return score
    #상대가 공을 놓칠 때마다 5점 추가
    elif ball.right == WINDOWWIDTH - LINETHICKNESS:
        score += 5
        return score
    #그 외 변화 없음
    else: return score

#AI of computer player
def artificialIntelligence(ball, ballDirX, paddle2):
    #공을 친 후엔 중앙으로 이동
    if ballDirX == LEFT:
        if paddle2.centery < (WINDOWHEIGHT/2):
            paddle2.y += INCREASESPEED
        elif paddle2.centery > (WINDOWHEIGHT/2):
            paddle2.y -= INCREASESPEED
    #공이 돌아올 때엔 공을 따라 이동
    elif ballDirX == RIGHT:
        if paddle2.centery < ball.centery:
            paddle2.y += INCREASESPEED
        else:
            paddle2.y -= INCREASESPEED
    return paddle2

#현재 점수 표시
def displayScore(score):
    resultSurf = BASICFONT.render('Score = %s' %(score), True, WHITE)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = (WINDOWWIDTH -150, 25)
    DISPLAYSURF.blit(resultSurf, resultRect)

#Main Function
def main():
    pygame.init()
    global DISPLAYSURF
    #폰트 정보
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    FPSCLOCK = pygame.time.Clock() #for set frame rate using variable FPS
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) #set game display
    pygame.display.set_caption('Pong') #set Title

    #변수 초기화 및 시작지점 설정
    ballX = WINDOWWIDTH/2 - LINETHICKNESS/2
    ballY = WINDOWHEIGHT/2 - LINETHICKNESS/2
    playerOnePosition = (WINDOWHEIGHT - PADDLESIZE) / 2
    playerTwoPosition = (WINDOWHEIGHT - PADDLESIZE) / 2
    score = 0

    #공의 방향 초기값
    ballDirX = LEFT # -1 = 왼쪽 / 1 = 오른쪽
    ballDirY= UP # -1 = 위 / 1 = 아래

    #공, 받침대 생성
    #인자 : 좌상단 x/y좌표, x/y길이
    paddle1 = pygame.Rect(PADDLEOFFSET,playerOnePosition,LINETHICKNESS,PADDLESIZE)
    paddle2 = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, playerTwoPosition, LINETHICKNESS, PADDLESIZE)
    ball = pygame.Rect(ballX,ballY, LINETHICKNESS,LINETHICKNESS)

    #모두 그려내기
    drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)

    #마우스 커서가 안 보이게 해 준다
    pygame.mouse.set_visible(0)

    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #마우스로 이동
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                paddle1.y = mousey

        drawArena()
        drawPaddle(paddle1)
        drawPaddle(paddle2)
        drawBall(ball)

        ball = moveBall(ball, ballDirX, ballDirY)
        ballDirX, ballDirY = checkEdgeCollision(ball, ballDirX, ballDirY)
        score = checkPointScored(paddle1, ball, score, ballDirX)
        ballDirX = ballDirX * checkHitBall(ball, paddle1, paddle2, ballDirX)
        paddle2 = artificialIntelligence(ball, ballDirX, paddle2)

        #displayScore(score)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == "__main__":
    main()
