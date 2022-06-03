import pygame
from character import CharacterAnimation
import os.path
from gameMap import Map, Pirate
import monster
from waterballoon import Bomb, Explode
from screen import Screen
from item import *

pygame.init()

screen = Screen()
screen.set_display()
board = [[0] * 13 for _ in range(13)]
clock = pygame.time.Clock()
cur_path = os.path.dirname(__file__)
asset_path = cur_path + '/../asset/'

# for img test #

# character_ss = Spritesheet(asset_path + 'character/animation.png')
character = CharacterAnimation('../asset/character/animation.png')
img = character.down_imgs[0]
dir = None

stage = Map()
soilder = monster.Soilder(asset_path + 'monster/soilder_sprite.png')
boss = monster.Boss(asset_path + 'monster/boss_sprite.png')
bomb = Bomb()
bomb_imgs = []
bombs = []
stage_num = 0
items = Item()
explosions = []
# test finished

running = True
while running:
	dt = clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				dir = 'left'
				character.move_flag = True
			elif event.key == pygame.K_RIGHT:
				dir = 'right'
				character.move_flag = True
			elif event.key == pygame.K_UP:
				dir = 'up'
				character.move_flag = True
			elif event.key == pygame.K_DOWN:
				dir = 'down'
				character.move_flag = True
			if event.key == pygame.K_SPACE:
				bomb_pos = character.balloon_pos()
				if stage.stages[stage_num][1][bomb_pos[1] // 40][bomb_pos[0] // 40] == -1:
					bombs.append([Bomb(), bomb_pos])
					stage.stages[stage_num][1][bomb_pos[1] // 40][bomb_pos[0] // 40] = 10
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				pass
			elif event.key == pygame.K_UP:
				if dir == 'up':
					character.move_flag = False
			elif event.key == pygame.K_DOWN:
				if dir == 'down':
					character.move_flag = False
			elif event.key == pygame.K_LEFT:
				if dir == 'left':
					character.move_flag = False
			elif event.key == pygame.K_RIGHT:
				if dir == 'right':
					character.move_flag = False
			img = character.down_imgs[0]
			character.img_idx = 0
	
	# 타일 깔기
	for y in range(13):
		for x, tile_idx in enumerate(stage.pirate.stage2_tile[y]):
			screen.window.blit(stage.pirate.tiles[tile_idx], 
			(x * 40 + screen.margin // 2, y * 40 + screen.margin // 2))

	# boss_img = boss.animation(boss.die_imgs, 0.1)
	# screen.window.blit(boss_img, (100, 100 + boss.y_pos))
	# soilder_img = soilder.animation(soilder.die_imgs, 0.1)
	# screen.window.blit(soilder_img, (50, 50))
	# bomb 깔기
	for b in bombs:
		if b[0].img_idx > 12:
			stage.stages[stage_num][1][b[1][1] // 40][b[1][0] // 40] = -1 # Center
			y_pos = b[1][1] // 40
			x_pos = b[1][0] // 40
			length = b[0].length
			bombs.pop(0)
			water_info = []
			explode = Explode()
			water_info.append(explode.explode(length, x_pos, y_pos, stage_num))
			water_info.append((x_pos, y_pos))
			explosions.append(water_info)
			explosions.append(explode)
		else:
			screen.window.blit(b[0].animation(bomb.bomb_imgs, 0.05), b[1])
	 

	# 블럭 깔기
	for y in range(13):
		for x in range(15):
			if 0 <= stage.stages[stage_num][1][y][x] < 10:
				block_list = stage.pirate.blocks[stage.stages[stage_num][1][y][x]]
				screen.window.blit(block_list[1],
				(x * 40 + screen.margin // 2, y * 40 + screen.margin // 2))
	
	# 폭발 처리
	for i in range(len(explosions)):
		screen.window.blit(explosions[1].explode_center[0], (explosions[0][1][0] * 40, explosions[0][1][1] * 40))
		if explode.explode_time > 100:
			explosions.pop(0)
		else:
			for y in range(explosions[0][1][1] - 1, explosions[0][1][1] - explosions[0][0][0]):
				screen.window.blit(explode.explode_up[4], (explosions[0][1][0] * 40, y * 40))
			for y in range(explosions[0][1][1] + 1, explosions[0][1][1] + explosions[0][0][1]):
				screen.window.blit(explode.explode_down[4], (explosions[0][1][0] * 40, y * 40))
			for x in range(explosions[0][1][0] - 1, explosions[0][1][0] - explosions[0][0][2]):
				screen.window.blit(explode.explode_left[4], (x * 40, explosions[0][1][1]))
			for x in range(explosions[0][1][0] + 1, explosions[0][1][0] + explosions[0][0][3]):
				screen.window.blit(explode.explode_right[4], (x * 40, explosions[0][1][1]))
			explosions[1].explode_time += 1

	# 캐릭터 애니메이션
	img = character.animation(0.2, dir)
	character.move_position(dir, stage_num)
	screen.window.blit(img, (character.x_pos, character.y_pos - 10)) # y pos 는 margin - 10 으로 해야함.
	
	for y in range(13):
		for x in range(15):
			if y < 12 and 0 <= stage.stages[stage_num][1][y + 1][x] < 10:
				block_list = stage.pirate.blocks[stage.stages[stage_num][1][y + 1][x]]
				screen.window.blit(block_list[0],
				(x * 40 + screen.margin // 2, y * 40 + 40 - block_list[2] + screen.margin // 2))

	# explode 구현
	# explode_up = explode.animation(explode.explode_up, 0.1)
	# screen.window.blit(explode_up, (100, 200))
	# explode_down = explode.animation(explode.explode_down, 0.1)
	# screen.window.blit(explode_down, (50, 200))
	pygame.display.update()
pygame.quit()