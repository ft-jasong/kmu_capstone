import pygame
from pygame.locals import DOUBLEBUF, QUIT, KEYUP, K_ESCAPE
import sys

pygame.init()

# 디스플레이 초기화
DISPLAYSURF = pygame.display.set_mode((624, 624), DOUBLEBUF)
pygame.display.set_caption("Stage 2")


# 맵 데이터: (1) 벽, (0) 바닥, (2) a tile (3) c tile (4) d tile (5) e tile (6) f tile (7) g tile

map_data = [
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 1, 2, 1, 2, 1, 3, 3, 3, 3],
    [3, 3, 3, 3, 2, 1, 2, 1, 2, 3, 3, 3, 3],
    [3, 3, 3, 3, 1, 2, 1, 2, 1, 3, 3, 3, 3],
    [3, 3, 3, 3, 2, 1, 2, 1, 2, 3, 3, 3, 3],
    [3, 5, 1, 2, 1, 2, 1, 2, 1, 2, 1, 5, 3],
    [3, 5, 2, 1, 2, 1, 2, 1, 2, 1, 2, 5, 3],
    [3, 5, 1, 2, 1, 2, 1, 2, 1, 2, 1, 5, 3],
    [3, 3, 3, 3, 2, 1, 2, 1, 2, 3, 3, 3, 3],
    [3, 3, 3, 3, 1, 2, 1, 2, 1, 3, 3, 3, 3],
    [3, 3, 3, 3, 2, 1, 2, 1, 2, 3, 3, 3, 3],
    [3, 3, 3, 3, 1, 2, 1, 2, 1, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
]

# 타일 이미지 로드
a = pygame.image.load("a.png").convert_alpha()
b = pygame.image.load("b.png").convert_alpha()
c = pygame.image.load("c.png").convert_alpha()

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
        else:
            tileImage = c
        cart_x = col_nb * TILEWIDTH
        cart_y = row_nb * TILEHEIGHT
        DISPLAYSURF.blit(tileImage, (cart_x, cart_y))

block_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 1, 0, 0, 0, 0, 0, 1, 2, 1, 0],
    [0, 0, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0, 0],
    [0, 1, 2, 1, 0, 0, 0, 0, 0, 1, 2, 1, 0],
    [0, 1, 2, 2, 0, 0, 2, 0, 0, 2, 2, 1, 0],
    [0, 3, 0, 0, 0, 2, 0, 2, 0, 0, 0, 3, 0],
    [0, 3, 1, 0, 2, 0, 2, 0, 2, 0, 1, 3, 0],
    [0, 3, 0, 0, 0, 2, 0, 2, 0, 0, 0, 3, 0],
    [0, 1, 2, 2, 0, 0, 2, 0, 0, 2, 2, 1, 0],
    [0, 1, 2, 1, 0, 0, 0, 0, 0, 1, 2, 1, 0],
    [0, 0, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0, 0],
    [0, 1, 2, 1, 0, 0, 0, 0, 0, 1, 2, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
house = pygame.image.load("kk.png").convert_alpha()
box = pygame.image.load("g.png").convert_alpha()
tree = pygame.image.load("nn.png").convert_alpha()

for row_nb, row in enumerate(block_data): 
    for col_nb, block in enumerate(row):
        if block == 1:
            blockImage = house
        elif block == 2:
            blockImage = box
        elif block == 3:
            blockImage = tree
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