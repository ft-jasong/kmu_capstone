import pygame
from character import CharacterAnimation
import os.path
from gameMap import Map, Pirate
import monster
from waterballoon import Bomb, Explode

class Screen(object):
	def __init__(self):
		self.margin = 40
		self.width = 600
		self.height = 520

	def set_display(self):
		self.window = pygame.display.set_mode((self.width + self.margin, self.height + self.margin))
		pygame.display.set_caption("Copy Crazy Arcade")
pygame.init()

screen = Screen()
screen.set_display()
board = [[0] * 13 for _ in range(13)]
clock = pygame.time.Clock()
cur_path = os.path.dirname(__file__)
asset_path = cur_path + '/../asset/'

# for img test #

# character_ss = Spritesheet(asset_path + 'character/animation.png')
Character = CharacterAnimation('../asset/character/animation.png')
img = Character.down_imgs[0]
dir = None
x_speed = 0
y_speed = 0
x_pos = 0
y_pos = 0

stage = Map()
soilder = monster.Soilder(asset_path + 'monster/soilder_sprite.png')
boss = monster.Boss(asset_path + 'monster/boss_sprite.png')
bomb = Bomb()
explode = Explode()
# test finished

running = True
while running:
	dt = clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				dir = Character.left_imgs
				x_speed = -3
				y_speed = 0
			elif event.key == pygame.K_RIGHT:
				dir = Character.right_imgs
				x_speed = 3
				y_speed = 0
			elif event.key == pygame.K_UP:
				dir = Character.up_imgs
				x_speed = 0
				y_speed = -3
			elif event.key == pygame.K_DOWN:
				dir = Character.down_imgs
				x_speed = 0
				y_speed = 3
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				if dir == Character.up_imgs:
					y_speed = 0
					x_speed = 0	
			if event.key == pygame.K_DOWN:
				if dir == Character.down_imgs:
					y_speed = 0
					x_speed = 0
			if event.key == pygame.K_LEFT:
				if dir == Character.left_imgs:
					y_speed = 0
					x_speed = 0
			if event.key == pygame.K_RIGHT:
				if dir == Character.right_imgs:
					y_speed = 0
					x_speed = 0
			img = Character.down_imgs[0]
			Character.img_idx = 0
	
	# 타일 깔기
	for y in range(13):
		for x, tile_idx in enumerate(stage.pirate.stage2_tile[y]):
			screen.window.blit(stage.pirate.tiles[tile_idx], 
			(screen.margin // 2 + x * 40, screen.margin // 2 + y * 40))
	
	# 캐릭터 애니메이션 -> 캐릭터가 블럭 뒤에 blit 되어야 하는데, 일단 편의상 이렇게 놔둠. 수정 필요.
	img = Character.animation(dir, 0.2)
	x_pos += x_speed
	y_pos += y_speed
	if x_pos < 0:
		x_pos = 0
	if y_pos < 0:
		y_pos = 0
	if x_pos > screen.width + screen.margin - 48:
		x_pos = screen.width + screen.margin - 48
	if y_pos > screen.height + screen.margin - 48:
		y_pos = screen.width + screen.margin - 48
	screen.window.blit(img, (x_pos, y_pos))

	# 블럭 깔기
	for y in range(13):
		for x in range(15):
			if stage.pirate.stage2_block[y][x] >= 0:
				block_list = stage.pirate.blocks[stage.pirate.stage2_block[y][x]]
				screen.window.blit(block_list[1],
				(screen.margin // 2 + x * 40, screen.margin // 2 + y * 40))
			if y < 12 and stage.pirate.stage2_block[y + 1][x] >= 0:
				block_list = stage.pirate.blocks[stage.pirate.stage2_block[y + 1][x]]
				screen.window.blit(block_list[0],
				(screen.margin // 2 + x * 40, screen.margin // 2 + y * 40 + 40 - block_list[2]))

	boss_img = boss.animation(boss.die_imgs, 0.1)
	screen.window.blit(boss_img, (100, 100 + boss.y_pos))
	soilder_img = soilder.animation(soilder.die_imgs, 0.1)
	screen.window.blit(soilder_img, (50, 50))
	bomb_img = bomb.animation(bomb.bomb_imgs, 0.1)
	screen.window.blit(bomb_img, (200, 200))
	explode_up = explode.animation(explode.explode_up, 0.1)
	screen.window.blit(explode_up, (100, 200))
	explode_down = explode.animation(explode.explode_down, 0.1)
	screen.window.blit(explode_down, (50, 200))
	pygame.display.update()
pygame.quit()