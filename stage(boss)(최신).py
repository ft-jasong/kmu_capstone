# -*- coding: utf-8 -*-
"""
Created on Fri May 20 03:13:18 2022

@author: blake
"""

import pygame
from pygame.locals import DOUBLEBUF, QUIT, KEYUP, K_ESCAPE
import sys

pygame.init()

# 디스플레이 초기화
DISPLAYSURF = pygame.display.set_mode((624, 624), DOUBLEBUF)
pygame.display.set_caption("Stage 2")


# 맵 데이터: (1) 벽, (0) 바닥, (2) a tile (3) c tile (4) d tile (5) e tile (6) f tile (7) g tile

map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 타일 이미지 로드
a = pygame.image.load("eee.png").convert_alpha()
b = pygame.image.load("hhh.png").convert_alpha()
c = pygame.image.load("ggg.png").convert_alpha()
d = pygame.image.load("fff.png").convert_alpha()
e = pygame.image.load("e.png").convert_alpha()

TILEWIDTH = 48  # 타일 너비
TILEHEIGHT = 48  # 타일 높이
TILEHEIGHT_HALF = TILEHEIGHT / 2
TILEWIDTH_HALF = TILEWIDTH / 2

# 타일 배치
for row_nb, row in enumerate(map_data):
    for col_nb, tile in enumerate(row):
        if tile == 1:
            tileImage = a
        elif tile == 2:
            tileImage = b
        elif tile == 3:
            tileImage = c
        elif tile == 4:
            tileImage = d
        elif tile == 5:
            tileImage = e
        else:
            tileImage = e
        cart_x = col_nb * TILEWIDTH
        cart_y = row_nb * TILEHEIGHT
        DISPLAYSURF.blit(tileImage, (cart_x, cart_y))

block_data = [
    [3, 4, 0, 4, 3, 4, 0, 4, 2, 4, 0, 4, 2],
    [3, 6, 5, 6, 3, 6, 5, 6, 2, 6, 5, 6, 2],
    [3, 7, 0, 7, 3, 7, 0, 7, 2, 7, 0, 7, 2],
    [3, 0, 0, 0, 3, 7, 0, 7, 2, 0, 0, 0, 2],
    [3, 0, 0, 8, 3, 0, 0, 0, 2, 8, 0, 0, 2],
    [3, 0, 0, 8, 3, 0, 0, 0, 2, 8, 0, 0, 2],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [3, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 2],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [3, 0, 10, 0, 0, 0, 0, 0, 0, 0, 10, 0, 2],
    [3, 10, 8, 8, 0, 0, 0, 0, 0, 8, 8, 10, 2],
    [3, 9, 10, 0, 0, 0, 0, 0, 0, 0, 10, 9, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

up = pygame.image.load("up.png").convert_alpha()
left = pygame.image.load("left_.png").convert_alpha()
right = pygame.image.load("right_.png").convert_alpha()
mmm = pygame.image.load("mmm.png").convert_alpha()
qwer = pygame.image.load("qwer.png").convert_alpha()
nnn = pygame.image.load("nnn.png").convert_alpha()
camp2 = pygame.image.load("campbox2.png").convert_alpha()
camp = pygame.image.load("campbox.png").convert_alpha()
jjj = pygame.image.load("jjj_.png").convert_alpha()
hhh = pygame.image.load("hhh.png").convert_alpha()

for row_nb, row in enumerate(block_data): 
    for col_nb, block in enumerate(row):
        if block == 1:
            blockImage = up
        elif block == 2:
            blockImage = left
        elif block == 3:
            blockImage = right
        elif block == 4:
            blockImage = mmm
        elif block == 5:
            blockImage = qwer
        elif block == 6:
            blockImage = nnn
        elif block == 7:
            blockImage = camp2
        elif block == 8:
            blockImage = camp
        elif block == 9:
            blockImage = jjj
        elif block == 10:
            blockImage = hhh
        else:
            continue
        cart_x = col_nb * TILEWIDTH
        cart_y = row_nb * TILEHEIGHT
        DISPLAYSURF.blit(blockImage, (cart_x, cart_y))
        

# 게임 실행
FPSCLOCK = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    FPSCLOCK.tick(30)