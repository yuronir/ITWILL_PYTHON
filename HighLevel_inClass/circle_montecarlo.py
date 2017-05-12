# 필요한 모듈
import pygame, sys
import random
from pygame.locals import *
import math


# 함수 생성(while 절에서 쓰임)
def Input(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit() #sys.exit(0) 전에 반드시 pygame.quit() 해주어야 한다.
            sys.exit(0)


# 변수 설정
dot_cnt = int(input('찍을 점의 개수 : '))  # 점 찍을 총 횟수
i = 0  # 점 찍기 수행횟수
cnt_in = 0  # 원 안에 들어간 횟수

# 출력 사이즈 설정
width = 600  # 점이 찍힐 정사각형 가로길이
height = 600  # 점이 찍힐 정사각형 세로길이
info_height = 50  # total_cnt, dot_cnt, cnt_in, pi 정보 출력란 사이즈
radius = int(width / 2)  # 원의 반지름

# 색깔 설정
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
white_red = (255, 200, 200)
white_blue = (200, 200, 255)
white_black = (200, 200, 200)

# 파이게임 설정
pygame.init()
pygame.display.set_caption('원주율(π) 구하기')
font = pygame.font.SysFont("Arial", 20, 0, 0)
window = pygame.display.set_mode((width, height + info_height))
screen = pygame.display.get_surface()  # 바탕화면을 변수 screen에 할당
screen.fill(white)  # 바탕화면 screen 의 색깔은 하얀색

# 배경화면 색깔 설정
pygame.draw.rect(screen, white_red, (0, 0, width, height), 0)  # 점이 찍힐 정사각형 부분은 연한 빨간색으로 설정
pygame.draw.circle(screen, white_blue, (radius, radius), radius, 0)  # 원 부분은 연한 파란색으로 설정
pygame.draw.rect(screen, white_black, (0, height, width, info_height), 0)  # 정보 출력란은 연한 검정색으로 설정

# 출력 위한 루프문
while True:
    Input(pygame.event.get())  # 위에서 생성한 input 함수

    if i >= dot_cnt:  # 점 찍은 횟수가 총 횟수보다 커지면 건너뜀
        continue
    else:  # 점 찍은 횟수가 총 횟수 미만이면 아래 작업 수행
        i += 1
        x = random.uniform(-radius, radius)  # 난수 생성. 원의 중심점을 (0,0)이라 했을 때 난수 생성 범위는 (-반지름 ~ 반지름) 사이
        y = random.uniform(-radius, radius)

        if math.pow(x, 2) + math.pow(y, 2) <= math.pow(radius, 2):  # 피타고라스 정리 이용하여 원 안에 점이 찍힌 경우를 판별
            cnt_in += 1
            pygame.draw.circle(screen, blue, (int(x + radius), int(y + radius)), 1, 0)  # 원 안에 점이 찍힌 경우 파란 점 찍기.
            # 이때 파이게임의 좌표는 좌측 상단의 좌표가 (0,0) 이므로
            # 범위가 (-반지름 ~ 반지름) 인 x, y 에 (+반지름) 해야함.
        else:
            pygame.draw.circle(screen, red, (int(x + radius), int(y + radius)), 1, 0)  # 원 안에 들어오지 않은 경우 빨간 점 찍기

    # while 루프 돌때마다 정보 출력란 리셋(안그러면 글자가 겹침)
    pygame.draw.rect(screen, white_black, (0, height + 1, width, height + info_height))

    # 정보 출력란 텍스트 생성
    text_total_cnt = font.render("Total_cnt: " + repr(dot_cnt), 1, (0, 0, 0))
    text_dot_cnt = font.render("Dot_cnt: " + repr(i), 1, (0, 0, 0))
    text_cnt_in = font.render("Cnt_in: " + repr(cnt_in), 1, (0, 0, 0))

    # 생성한 텍스르 출력
    screen.blit(text_total_cnt,
                (1 * width / 24, height + (info_height / 3)))  # (1*width/24,height + (info_height/3))부분은 출력 위치 좌표
    screen.blit(text_dot_cnt, (7 * width / 24, height + (info_height / 3)))
    screen.blit(text_cnt_in, (13 * width / 24, height + (info_height / 3)))

    # 파이 계산 및 텍스트 출력(try 와 except 절 안 써도 출력 가능)
    try:
        pi = repr(round((cnt_in / i) * 4, 6))
        text_pi = font.render("π : " + pi, 1, (0, 0, 0))
        screen.blit(text_pi, (19 * width / 24, height + (info_height / 3)))

    except ZeroDivisixxxxxxonError as message:
        print(message)

    pygame.display.flip()
