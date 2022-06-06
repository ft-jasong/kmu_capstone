import pygame
from character import CharacterAnimation
import os.path
from gameMap import Map
import monster
from waterballoon import Bomb, Explode
from screen import Screen
from item import *
from monster import *

def soilder_explode_collide(soilders, exp_rect):
	for i in range(len(soilders)):
		soilders[i].rect = soilders[i].img.get_rect()
		soilders[i].rect.left = soilders[i].x_pos
		soilders[i].rect.top = soilders[i].y_pos
		if soilders[i].rect.colliderect(exp_rect):
			soilders[i].die_flag = True
			soilders[i].move_flag = False
			
def boss_explode_collide(boss_rect, exp_rect):
	# print(boss_rect.colliderect(exp_rect))
	if boss_rect.colliderect(exp_rect):
		boss.hit()

# def prepare_soilders(stage_num):
# 	if stage_num == 0:
# 		soilders = [Soilder(asset_path + 'monster/soilder_sprite.png', x, y) for x, y in stage1_soilder_pos]
# 	elif stage_num == 1:
# 		soilders = [Soilder(asset_path + 'monster/soilder_sprite.png', x, y) for x, y in stage2_soilder_pos]
# 	else:
# 		soilders = []
pygame.init()
pygame.mixer.init()

screen = Screen()
screen.set_display()
board = [[0] * 13 for _ in range(13)]
clock = pygame.time.Clock()
cur_path = os.path.dirname(__file__)
asset_path = cur_path + '/../asset/'
sound_path = asset_path + 'sound/'
item_sound = pygame.mixer.Sound(sound_path + 'ItemGet.mp3')
inballoon_sound = pygame.mixer.Sound(sound_path + 'inBalloon.mp3')
balloon_explode_sound = pygame.mixer.Sound(sound_path + 'balloon_explosion.mp3')
bomb_boom_sound = pygame.mixer.Sound(sound_path + 'bomb_explosion.mp3')
drop_bomb_sound = pygame.mixer.Sound(sound_path + 'dropBomb.mp3')
gamestart_sound = pygame.mixer.Sound(sound_path + 'game_start.mp3')

# for img test #

character = CharacterAnimation('../asset/character/animation.png')
img = character.down_imgs[0]
dir = None

stage = Map()
# soilder = monster.Soilder(asset_path + 'monster/soilder_sprite.png', 0, 200)
soilders = []
stage1_soilder_pos = [
	(0,0), (6*40, 1*40), (8*40,1*40), (7*40,3*40), (5*40,6*40), (9*40,6*40), (7*40,9*40), (14*40, 12*40)
]
stage2_soilder_pos = [
	(0*40,2*40), (1*40,2*40), (4*40,2*40), (5*40,1*40), (7*40,1*40), (9*40,1*40), (11*40,2*40), (13*40,2*40), (14*40,2*40)
]
# soilders.append(soilder)
mob = []
boss = monster.Boss(asset_path + 'monster/boss_sprite.png')
bomb_imgs = []
bombs = []
bomb = Bomb(character.bomb_len)
stage_num = -1
items = Item()
explosions = []
# test finished

running = True
while running:
	dt = clock.tick(60)
	screen.window.blit(screen.background, (0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if stage_num < 0:
				gamestart_sound.play()
				# stage_num = 2 #이거 주석 풀면 보스
				# soilders = [] # 보스 바로가기
				stage_num += 1 
				soilders = [Soilder(asset_path + 'monster/soilder_sprite.png', x, y) for x, y in stage1_soilder_pos]
				character.default_character_state(stage_num)
			if character.die_state is False and character.bubble_state is False:
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
					if stage.stages[stage_num][1][bomb_pos[1] // 40][bomb_pos[0] // 40] <= -1:
						if len(bombs) < character.max_bomb:
							bombs.append([Bomb(character.bomb_len), bomb_pos])
							stage.stages[stage_num][1][bomb_pos[1] // 40][bomb_pos[0] // 40] = 10
							drop_bomb_sound.play()
			else:
				character.move_flag = False
		if event.type == pygame.KEYUP:
			if character.die_state is False and character.bubble_state is False:
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
			else:
				character.move_flag = False
	
	# 타일 깔기
	if stage_num < 0:
		screen.window.blit(screen.main_logo, (175, 50))
	elif 0 <= stage_num < 3:
		for y in range(13):
			for x, tile_idx in enumerate(stage.stages[stage_num][0][y]):
				screen.window.blit(stage.pirate.tiles[tile_idx], 
				(x * 40 + screen.margin // 2, y * 40 + screen.margin // 2))
		
		# soilder_img = soilder.animation(soilder.move_imgs, 0.1)
		# screen.window.blit(soilder_img, (soilder.x_pos, soilder.y_pos))
		# bomb 깔기
		for b in bombs:
			if b[0].img_idx > 12:
				stage.stages[stage_num][1][b[1][1] // 40][b[1][0] // 40] = -1 # Center
				y_pos = b[1][1] // 40
				x_pos = b[1][0] // 40
				length = b[0].length
				bombs.pop(0)
				bomb_boom_sound.play()
				water_info = []
				explode = Explode()
				water_info.append(explode.explode(length, x_pos, y_pos, stage_num))
				water_info.append((x_pos, y_pos))
				water_info.append(explode)
				explosions.append(water_info)
			else:
				screen.window.blit(b[0].animation(bomb.bomb_imgs, 0.05), b[1])
		if stage_num == 2:
			boss_soilder_pos = boss.summon_soilder(len(soilders))
			if boss_soilder_pos != None:
				soilders.append(Soilder(asset_path + 'monster/soilder_sprite.png', boss_soilder_pos[0], boss_soilder_pos[1]))
			boss.move()
			screen.window.blit(boss.img, (boss.x_pos + boss.blit_x, boss.y_pos + boss.blit_y))
		# boss_img = boss.animation(boss.attack_imgs, 0.1)

		# 블럭 깔기
		for y in range(13):
			for x in range(15):
				if 0 <= stage.stages[stage_num][1][y][x] < 10:
					block_list = stage.pirate.blocks[stage.stages[stage_num][1][y][x]]
					screen.window.blit(block_list[1],
					(x * 40 + screen.margin // 2, y * 40 + screen.margin // 2))
				elif stage.stages[stage_num][1][y][x] <= -80:
					idx = stage.stages[stage_num][1][y][x] + 85
					if idx < 4:
						img = items.pirate_item.items[idx]
						screen.window.blit(img,
						(x * 40 + screen.margin // 2, y * 40 + screen.margin // 2))
					else:
						pass
		
		# 폭발 처리
		for e in explosions:
			if e[2].explode_time > 100:
				explosions.pop(0)
			else:
				idx = (e[2].explode_time) // 10 % 3
				character_rect = img.get_rect()
				character_rect.top = character.y_pos + 10
				character_rect.left = character.x_pos
				exp_img = e[2].explode_center[idx]
				exp_img_rect = exp_img.get_rect()
				exp_img_rect.left = e[1][0] * 40 + Screen.margin // 2
				exp_img_rect.top = e[1][1] * 40 + Screen.margin // 2
				if exp_img_rect.colliderect(character_rect):
					if character.bubble_state is False:
						inballoon_sound.play()
					character.bubble_state = True
					character.move_flag = False
				soilder_explode_collide(soilders, exp_img_rect)
				if stage_num == 2 and boss.die_flag is False:
					# # print('boss colide check')
					boss.rect = boss.img.get_rect()
					boss.rect.left = boss.x_pos
					boss.rect.top = boss.y_pos
					boss_explode_collide(exp_img_rect, boss.rect)
				screen.window.blit(e[2].explode_center[idx], (e[1][0] * 40 + Screen.margin // 2, e[1][1] * 40 + Screen.margin // 2))
				for y in range(e[1][1] - 1, e[1][1] - e[0][0] - 1, -1):
					if y ==  e[1][1] - e[0][0]:
						idx = (e[2].explode_time) // 10 % 2
						if e[2].explode_time <= 70:
							screen.window.blit(explode.explode_up[idx], (e[1][0] * 40 + Screen.margin // 2, y * 40 + Screen.margin // 2))
							exp_img = e[2].explode_up[idx]
							exp_img_rect = exp_img.get_rect()
							exp_img_rect.left = e[1][0] * 40 + Screen.margin // 2
							exp_img_rect.top = y * 40 + Screen.margin // 2
							if exp_img_rect.colliderect(character_rect):
								character.bubble_state = True
								character.move_flag = False
							soilder_explode_collide(soilders, exp_img_rect)
							if stage_num == 2 and boss.die_flag is False:
								# # print('boss colide check')
								boss.rect = boss.img.get_rect()
								boss.rect.left = boss.x_pos
								boss.rect.top = boss.y_pos
								boss_explode_collide(exp_img_rect, boss.rect)
						else:
							idx = ((e[2].explode_time) - 61) // 10
							screen.window.blit(explode.explode_up[idx], (e[1][0] * 40 + Screen.margin // 2, y * 40 + Screen.margin // 2))
							exp_img = e[2].explode_up[idx]
							exp_img_rect = exp_img.get_rect()
							exp_img_rect.left = e[1][0] * 40 + Screen.margin // 2
							exp_img_rect.top = y * 40 + Screen.margin // 2
							if exp_img_rect.colliderect(character_rect):
								character.bubble_state = True
								character.move_flag = False
							soilder_explode_collide(soilders, exp_img_rect)
							if stage_num == 2 and boss.die_flag is False:
								# # print('boss colide check')
								boss.rect = boss.img.get_rect()
								boss.rect.left = boss.x_pos
								boss.rect.top = boss.y_pos
								boss_explode_collide(exp_img_rect, boss.rect)
					else:
						screen.window.blit(explode.explode_up[4], (e[1][0] * 40 + Screen.margin // 2, y * 40 + Screen.margin // 2))
						exp_img = e[2].explode_up[4]
						exp_img_rect = exp_img.get_rect()
						exp_img_rect.left = e[1][0] * 40 + Screen.margin // 2
						exp_img_rect.top = y * 40 + Screen.margin // 2
						if exp_img_rect.colliderect(character_rect):
							character.bubble_state = True
							character.move_flag = False
						soilder_explode_collide(soilders, exp_img_rect)
						if stage_num == 2 and boss.die_flag is False:
							# # print('boss colide check')
							boss.rect = boss.img.get_rect()
							boss.rect.left = boss.x_pos
							boss.rect.top = boss.y_pos
							boss_explode_collide(exp_img_rect, boss.rect)
				for y in range(e[1][1] + 1, e[1][1] + e[0][1] + 1):
					if y ==  e[1][1] + e[0][1]:
						idx = (e[2].explode_time) // 10 % 2
						if e[2].explode_time <= 70:
							screen.window.blit(explode.explode_down[idx], (e[1][0] * 40 + Screen.margin // 2, y * 40 + Screen.margin // 2))
							exp_img = e[2].explode_down[idx]
							exp_img_rect = exp_img.get_rect()
							exp_img_rect.left = e[1][0] * 40 + Screen.margin // 2
							exp_img_rect.top = y * 40 + Screen.margin // 2
							if exp_img_rect.colliderect(character_rect):
								character.bubble_state = True
								character.move_flag = False
							soilder_explode_collide(soilders, exp_img_rect)
							if stage_num == 2 and boss.die_flag is False:
								# # print('boss colide check')
								boss.rect = boss.img.get_rect()
								boss.rect.left = boss.x_pos
								boss.rect.top = boss.y_pos
								boss_explode_collide(exp_img_rect, boss.rect)
						else:
							idx = ((e[2].explode_time) - 61) // 10
							screen.window.blit(explode.explode_down[idx], (e[1][0] * 40 + Screen.margin // 2, y * 40 + Screen.margin // 2))
							exp_img = e[2].explode_down[idx]
							exp_img_rect = exp_img.get_rect()
							exp_img_rect.left = e[1][0] * 40 + Screen.margin // 2
							exp_img_rect.top = y * 40 + Screen.margin // 2
							if exp_img_rect.colliderect(character_rect):
								character.bubble_state = True
								character.move_flag = False
							soilder_explode_collide(soilders, exp_img_rect)
							if stage_num == 2 and boss.die_flag is False:
								# # print('boss colide check')
								boss.rect = boss.img.get_rect()
								boss.rect.left = boss.x_pos
								boss.rect.top = boss.y_pos
								boss_explode_collide(exp_img_rect, boss.rect)
					else:
						screen.window.blit(explode.explode_down[4], (e[1][0] * 40 + Screen.margin // 2, y * 40 + Screen.margin // 2))
						exp_img = e[2].explode_down[4]
						exp_img_rect = exp_img.get_rect()
						exp_img_rect.left = e[1][0] * 40 + Screen.margin // 2
						exp_img_rect.top = y * 40 + Screen.margin // 2
						if exp_img_rect.colliderect(character_rect):
							character.bubble_state = True
							character.move_flag = False
						soilder_explode_collide(soilders, exp_img_rect)
						if stage_num == 2 and boss.die_flag is False:
							# # print('boss colide check')
							boss.rect = boss.img.get_rect()
							boss.rect.left = boss.x_pos
							boss.rect.top = boss.y_pos
							boss_explode_collide(exp_img_rect, boss.rect)
				for x in range(e[1][0] - 1, e[1][0] - e[0][2] - 1, -1):
					if x == e[1][0] - e[0][2]:
						idx = (e[2].explode_time) // 10 % 2
						if e[2].explode_time <= 70:
							screen.window.blit(explode.explode_left[idx], (x * 40 + Screen.margin // 2, e[1][1] * 40 + Screen.margin // 2))
							exp_img = e[2].explode_left[idx]
							exp_img_rect = exp_img.get_rect()
							exp_img_rect.left = x * 40 + Screen.margin // 2
							exp_img_rect.top = e[1][1] * 40 + Screen.margin // 2
							if exp_img_rect.colliderect(character_rect):
								character.bubble_state = True
								character.move_flag = False
							soilder_explode_collide(soilders, exp_img_rect)
							if stage_num == 2 and boss.die_flag is False:
								# # print('boss colide check')
								boss.rect = boss.img.get_rect()
								boss.rect.left = boss.x_pos
								boss.rect.top = boss.y_pos
								boss_explode_collide(exp_img_rect, boss.rect)
						else:
							idx = ((e[2].explode_time) - 61) // 10
							screen.window.blit(explode.explode_left[idx], (x * 40 + Screen.margin // 2, e[1][1] * 40 + Screen.margin // 2))
							exp_img = e[2].explode_left[idx]
							exp_img_rect = exp_img.get_rect()
							exp_img_rect.left = x * 40 + Screen.margin // 2
							exp_img_rect.top = e[1][1] * 40 + Screen.margin // 2
							if exp_img_rect.colliderect(character_rect):
								character.bubble_state = True
								character.move_flag = False
							soilder_explode_collide(soilders, exp_img_rect)
							if stage_num == 2 and boss.die_flag is False:
								# # print('boss colide check')
								boss.rect = boss.img.get_rect()
								boss.rect.left = boss.x_pos
								boss.rect.top = boss.y_pos
								boss_explode_collide(exp_img_rect, boss.rect)
					else:
						screen.window.blit(explode.explode_left[4], (x * 40 + Screen.margin // 2, e[1][1] * 40 + Screen.margin // 2))
						exp_img = e[2].explode_left[4]
						exp_img_rect = exp_img.get_rect()
						exp_img_rect.left = x * 40 + Screen.margin // 2
						exp_img_rect.top = e[1][1] * 40 + Screen.margin // 2
						if exp_img_rect.colliderect(character_rect):
							character.bubble_state = True
							character.move_flag = False
						soilder_explode_collide(soilders, exp_img_rect)
						if stage_num == 2 and boss.die_flag is False:
							# # print('boss colide check')
							boss.rect = boss.img.get_rect()
							boss.rect.left = boss.x_pos
							boss.rect.top = boss.y_pos
							boss_explode_collide(exp_img_rect, boss.rect)
				for x in range(e[1][0] + 1, e[1][0] + e[0][3] + 1):
					if x == e[1][0] + e[0][3]:
						idx = (e[2].explode_time) // 10 % 2
						if e[2].explode_time <= 70:
							screen.window.blit(explode.explode_right[idx], (x * 40 + Screen.margin // 2, e[1][1] * 40 + Screen.margin // 2))
							exp_img = e[2].explode_right[idx]
							exp_img_rect = exp_img.get_rect()
							exp_img_rect.left = x * 40 + Screen.margin // 2
							exp_img_rect.top = e[1][1] * 40 + Screen.margin // 2
							if exp_img_rect.colliderect(character_rect):
								character.bubble_state = True
								character.move_flag = False
							soilder_explode_collide(soilders, exp_img_rect)
							if stage_num == 2 and boss.die_flag is False:
								# # print('boss colide check')
								boss.rect = boss.img.get_rect()
								boss.rect.left = boss.x_pos
								boss.rect.top = boss.y_pos
								boss_explode_collide(exp_img_rect, boss.rect)
						else:
							idx = ((e[2].explode_time) - 61) // 10
							screen.window.blit(explode.explode_right[idx], (x * 40 + Screen.margin // 2, e[1][1] * 40 + Screen.margin // 2))
							exp_img = e[2].explode_right[idx]
							exp_img_rect = exp_img.get_rect()
							exp_img_rect.left = x * 40 + Screen.margin // 2
							exp_img_rect.top = e[1][1] * 40 + Screen.margin // 2
							if exp_img_rect.colliderect(character_rect):
								character.bubble_state = True
								character.move_flag = False
							soilder_explode_collide(soilders, exp_img_rect)
							if stage_num == 2 and boss.die_flag is False:
								# # print('boss colide check')
								boss.rect = boss.img.get_rect()
								boss.rect.left = boss.x_pos
								boss.rect.top = boss.y_pos
								boss_explode_collide(exp_img_rect, boss.rect)
					else:
						screen.window.blit(explode.explode_right[4], (x * 40 + Screen.margin // 2, e[1][1] * 40 + Screen.margin // 2))
						exp_img = e[2].explode_right[4]
						exp_img_rect = exp_img.get_rect()
						exp_img_rect.left = x * 40 + Screen.margin // 2
						exp_img_rect.top = e[1][1] * 40 + Screen.margin // 2
						if exp_img_rect.colliderect(character_rect):
							character.bubble_state = True
							character.move_flag = False
						soilder_explode_collide(soilders, exp_img_rect)
						if stage_num == 2 and boss.die_flag is False:
							# # print('boss colide check')
							boss.rect = boss.img.get_rect()
							boss.rect.left = boss.x_pos
							boss.rect.top = boss.y_pos
							boss_explode_collide(exp_img_rect, boss.rect)
				e[2].explode_time += 2

		# 캐릭터 애니메이션
		img = character.animation(0.2, dir)
		character.move_position(dir, stage_num)
		character.item_get_check(stage_num, item_sound)
		# 캐릭터 - 병사 충돌
		for idx, s in enumerate(soilders):
			if s.die_flag is False:
				s.move(stage_num)
				character_rect = img.get_rect()
				character_rect.top = character.y_pos
				character_rect.left = character.x_pos
				s.rect = s.img.get_rect()
				s.rect.left = s.x_pos
				s.rect.top = s.y_pos + 10
				if s.rect.colliderect(character_rect):
					character.die_state = True
					character.move_flag = False
				soilder_img = s.animation(s.move_imgs, 0.1)
				screen.window.blit(soilder_img, (s.x_pos, s.y_pos))
			elif s.die_idx >= 4:
				soilders.pop(idx)
			elif s.die_idx < 4:
				soilder_img = s.animation(s.move_imgs, 0.1)
				screen.window.blit(soilder_img, (s.x_pos, s.y_pos))
		# 보스 - 캐릭터 충돌
		if stage_num == 2 and boss.die_flag is False:
			character_rect = img.get_rect()
			character_rect.top = character.y_pos
			character_rect.left = character.x_pos
			boss.rect = boss.img.get_rect()
			boss.rect.top = boss.y_pos
			boss.rect.left = boss.x_pos
			if boss.rect.colliderect(character_rect):
				character.move_flag = False
				character.die_state = True
		screen.window.blit(img, (character.x_pos, character.y_pos - 10)) # y pos 는 margin - 10 으로 해야함.
		
		if stage_num == 2 and boss.die_flag is True:
			if boss.die_idx >= 4:
				running = False
			else:
				boss.die_animation()
		for y in range(13):
			for x in range(15):
				if y < 12 and 0 <= stage.stages[stage_num][1][y + 1][x] < 10:
					block_list = stage.pirate.blocks[stage.stages[stage_num][1][y + 1][x]]
					screen.window.blit(block_list[0],
					(x * 40 + screen.margin // 2, y * 40 + 40 - block_list[2] + screen.margin // 2))
		if stage_num <= 1:
			if len(soilders) <= 0:
				stage_num += 1
				if stage_num == 1:
					soilders = [Soilder(asset_path + 'monster/soilder_sprite.png', x, y) for x, y in stage2_soilder_pos]
					bombs = []
				elif stage_num == 2:
					soilders = []
					bombs = []
				character.default_character_state(stage_num)
		if character.die_idx >= 6:
			running = False
	pygame.display.update()
pygame.quit()