# -*- coding: utf-8 -*-
"""
Created on Fri May 20 02:32:49 2022

@author: blake
"""


# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:43:11 2022

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
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
a = pygame.image.load("blue.png").convert_alpha()

TILEWIDTH = 48  # 타일 너비
TILEHEIGHT = 48  # 타일 높이
TILEHEIGHT_HALF = TILEHEIGHT / 2
TILEWIDTH_HALF = TILEWIDTH / 2

# 타일 배치
for row_nb, row in enumerate(map_data):
    for col_nb, tile in enumerate(row):
        if tile == 1:
            tileImage = a
        else:
            tileImage = a
        cart_x = col_nb * TILEWIDTH
        cart_y = row_nb * TILEHEIGHT
        DISPLAYSURF.blit(tileImage, (cart_x, cart_y))

block_data = [
    [2, 0, 3, 0, 0, 1, 3, 1, 0, 0, 3, 0, 2],
    [3, 0, 0, 3, 0, 0, 6, 0, 0, 3, 0, 0, 3],
    [2, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 2],
    [3, 5, 0, 3, 0, 0, 0, 0, 0, 3, 0, 5, 3],
    [2, 0, 0, 1, 0, 0, 3, 0, 0, 1, 0, 0, 2],
    [3, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 3],
    [2, 6, 6, 0, 3, 4, 1, 4, 3, 0, 6, 6, 2],
    [3, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 3],
    [2, 0, 0, 1, 0, 0, 3, 0, 0, 1, 0, 0, 2],
    [3, 5, 0, 3, 0, 0, 0, 0, 0, 3, 0, 5, 3],
    [2, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 2],
    [3, 0, 0, 3, 0, 0, 6, 0, 0, 3, 0, 0, 3],
    [2, 0, 3, 0, 0, 1, 3, 1, 0, 0, 3, 0, 2]
    ]

yellowbox = pygame.image.load("yellowbox.png").convert_alpha()
greenbox = pygame.image.load("orangebox.png").convert_alpha()
icebox = pygame.image.load("bb.png").convert_alpha()
box = pygame.image.load("j.png").convert_alpha()
mo = pygame.image.load("mo.png").convert_alpha()
h = pygame.image.load("h.png").convert_alpha()

for row_nb, row in enumerate(block_data): 
    for col_nb, block in enumerate(row):
        if block == 1:
            blockImage = yellowbox
        elif block == 2:
            blockImage = greenbox
        elif block == 3:
            blockImage = icebox
        elif block == 4:
            blockImage = mo
        elif block == 5:
            blockImage = h
        elif block == 6:
            blockImage = box
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