import pygame
from character import CharacterAnimation
import os.path
from gameMap import Map, Pirate
import monster
from waterballoon import Bomb, Explode
from screen import Screen

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
explode = Explode()
stage_idx = 0
bomb_imgs = []
bombs = []
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
				bombs.append([Bomb(), character.balloon_pos()])
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
		if b[0].img_idx > 7:
			bombs.pop(0)
		else:
			screen.window.blit(b[0].animation(bomb.bomb_imgs, 0.1), b[1])
	# 블럭 깔기
	for y in range(13):
		for x in range(15):
			if stage.pirate.stage2_block[y][x] >= 0:
				block_list = stage.pirate.blocks[stage.pirate.stage2_block[y][x]]
				screen.window.blit(block_list[1],
				(x * 40 + screen.margin // 2, y * 40 + screen.margin // 2))
			if y < 12 and stage.pirate.stage2_block[y + 1][x] >= 0:
				block_list = stage.pirate.blocks[stage.pirate.stage2_block[y + 1][x]]
				screen.window.blit(block_list[0],
				(x * 40 + screen.margin // 2, y * 40 + 40 - block_list[2] + screen.margin // 2))
	
	# 캐릭터 애니메이션 -> 캐릭터가 블럭 뒤에 blit 되어야 하는데, 일단 편의상 이렇게 놔둠. 수정 필요.
	img = character.animation(0.2, dir)
	character.move_position(dir, 1)
	screen.window.blit(img, (character.x_pos, character.y_pos - 10)) # y pos 는 margin - 10 으로 해야함.
	
	# explode 구현
	# explode_up = explode.animation(explode.explode_up, 0.1)
	# screen.window.blit(explode_up, (100, 200))
	# explode_down = explode.animation(explode.explode_down, 0.1)
	# screen.window.blit(explode_down, (50, 200))
	pygame.display.update()
pygame.quit()