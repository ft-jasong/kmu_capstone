import pygame
import spritesheet as ss
import os.path
from screen import Screen
from gameMap import Map

class CharacterAnimation(object):
	def init_up_imgs(self):
		self.up_imgs.append(pygame.transform.scale(self.sprite_img.image_at((438, 1, 44, 56), colorkey= -1), (40, 50)))
		self.up_imgs.append(pygame.transform.scale(self.sprite_img.image_at((587, 59, 44, 55), colorkey= -1), (40, 50)))
		self.up_imgs.append(pygame.transform.scale(self.sprite_img.image_at((498, 59, 43, 56), colorkey= -1), (40, 50)))
		self.up_imgs.append(pygame.transform.scale(self.sprite_img.image_at((438, 1, 44, 56), colorkey= -1), (40, 50)))
		self.up_imgs.append(pygame.transform.scale(self.sprite_img.image_at((618, 1, 44, 55), colorkey= -1), (40, 50)))
		self.up_imgs.append(pygame.transform.scale(self.sprite_img.image_at((529, 1, 43, 56), colorkey= -1), (40, 50)))

	def init_down_imgs(self):
		self.down_imgs.append(pygame.transform.scale(self.sprite_img.image_at((305, 1, 42, 57), colorkey= - 1), (40, 50)))
		self.down_imgs.append(pygame.transform.scale(self.sprite_img.image_at((392, 1, 44, 56), colorkey= - 1), (40, 50)))
		self.down_imgs.append(pygame.transform.scale(self.sprite_img.image_at((664, 1, 42, 55), colorkey= - 1), (40, 50)))
		self.down_imgs.append(pygame.transform.scale(self.sprite_img.image_at((320, 60, 42, 57), colorkey= - 1), (40, 50)))
		self.down_imgs.append(pygame.transform.scale(self.sprite_img.image_at((392, 1, 44, 56), colorkey= - 1), (40, 50)))
		self.down_imgs.append(pygame.transform.scale(self.sprite_img.image_at((633, 58, 44, 56), colorkey= - 1), (40, 50)))

	def init_left_imgs(self):
		self.left_imgs = [pygame.transform.flip(img, True, False) for img in self.right_imgs]

	def init_right_imgs(self):
		self.right_imgs.append(pygame.transform.scale(self.sprite_img.image_at((262, 1, 41, 58), colorkey= - 1), (40, 50)))
		self.right_imgs.append(pygame.transform.scale(self.sprite_img.image_at((574, 1, 41, 57), colorkey= - 1), (40, 50)))
		self.right_imgs.append(pygame.transform.scale(self.sprite_img.image_at((484, 1, 43, 56), colorkey= - 1), (40, 50)))
		self.right_imgs.append(pygame.transform.scale(self.sprite_img.image_at((274, 61, 44, 57), colorkey= - 1), (40, 50)))
		self.right_imgs.append(pygame.transform.scale(self.sprite_img.image_at((484, 1, 43, 56), colorkey= - 1), (40, 50)))
		self.right_imgs.append(pygame.transform.scale(self.sprite_img.image_at((364, 60, 41, 57), colorkey= - 1), (40, 50)))

	def init_stop_imgs(self):
		self.down_stop = pygame.transform.scale(self.sprite_img.image_at((391, 0, 46, 58), -1), (40, 50))
		self.up_stop = pygame.transform.scale(self.sprite_img.image_at((437, 0, 46, 58), -1), (40, 50))
		self.left_stop = pygame.transform.scale(self.sprite_img.image_at((348, 0, 43, 59), -1), (40, 50))
		self.right_stop = pygame.transform.scale(self.sprite_img.image_at((483, 0, 45, 58), -1), (40, 50))

	def init_die_imgs(self):
		self.die_imgs = self.die_sprite.load_strip((0, 0, 70, 70), 16, colorkey=-1)
		self.die_imgs = [pygame.transform.scale(img, (50, 50)) for img in self.die_imgs]

	def init_bubble_imgs(self):
		self.bubble_imgs = self.bubble_sprite.load_strip((0, 0, 60, 60), 16, colorkey=-1)
		self.bubble_imgs = [pygame.transform.scale(img, (50, 50)) for img in self.bubble_imgs]

	def init_all_imgs(self):
		self.init_up_imgs()
		self.init_right_imgs()
		self.init_down_imgs()
		self.init_left_imgs()
		self.init_stop_imgs()
		self.init_bubble_imgs()
		self.init_die_imgs()
		self.ani_imgs = self.down_imgs

	def __init__(self, rel_path):
		self.cur_dir = os.path.dirname(__file__)
		self.img_path = self.cur_dir + '/' + rel_path
		self.sprite_img = ss.Spritesheet(self.img_path)
		self.bubble_sprite = ss.Spritesheet(self.cur_dir + '/../asset/character/bazziBubble.bmp')
		self.die_sprite = ss.Spritesheet(self.cur_dir + '/../asset/character/bazziDie.bmp')
		self.up_imgs = []
		self.down_imgs = []
		self.left_imgs = []
		self.right_imgs = []
		self.ani_imgs = []
		self.die_imgs = []
		self.img_idx = 0
		self.x_pos = Screen.margin // 2
		self.y_pos = Screen.margin // 2
		self.speed = 5
		self.move_flag = False
		self.left_stop = None
		self.right_stop = None
		self.up_stop = None
		self.down_stop = None
		self.bomb_len = 2
		self.max_bomb_len = 7
		self.max_bomb = 1
		self.max_bomb_count = 9
		self.center_x = Screen.margin
		self.center_y = Screen.margin
		self.bubble_imgs = []
		self.bubble_idx = 0
		self.bubble_state = False
		self.die_state = False
		self.die_idx = 0
		self.init_all_imgs()

	def animation(self, speed, dir):
		if self.die_state is True:
			self.die_idx += speed / 2
			# if self.die_idx >= 7:
			# 	return None
			return self.die_imgs[int(self.die_idx) % 7]
		elif self.bubble_state is True:
			self.bubble_idx += speed / 2
			if self.bubble_idx >= 16:
				self.die_state = True
				self.bubble_state = False
			return self.bubble_imgs[int(self.bubble_idx) % 16]
		elif self.move_flag == True:
			self.img_idx += speed
			character_img = self.ani_imgs[int(self.img_idx % len(self.ani_imgs))]
			return character_img
		else:
			if dir == 'left':
				return self.left_stop
			elif dir == 'right':
				return self.right_stop
			elif dir == 'up':
				return self.up_stop
			elif dir == 'down':
				return self.down_stop
			else:
				return self.down_stop

	def item_get_check(self, stage_num):
		cur_x = round(self.center_x - 0.44) // 40
		cur_y = round(self.center_y - 0.38) // 40
		item_idx = Map.stages[stage_num][1][cur_y][cur_x] + 85
		if 0 <= item_idx < 10:
			if 0 <= item_idx < 4:
				if item_idx == 0:
					if self.max_bomb < self.max_bomb_count:
						self.max_bomb += 1
					# bgm
				elif item_idx == 1:
					self.speed += 1
					# bgm
				elif item_idx == 2:
					if self.bomb_len < self.max_bomb_len:
						self.bomb_len += 1
					# bgm
				elif item_idx == 3:
					self.bomb_len = self.max_bomb_len
			Map.stages[stage_num][1][cur_y][cur_x] = -1

	def move_position(self, dir, stage_num):
		half_margin = Screen.margin // 2
		cur_rect = (
			self.x_pos - half_margin, self.y_pos + 10 - half_margin,
			self.x_pos + 39 - half_margin, self.y_pos + 18 + 32 - half_margin
			)
		self.center_x = (cur_rect[0] + cur_rect[2]) / 2
		self.center_y = (cur_rect[1] + cur_rect[3]) / 2
		if self.move_flag is True:
			if dir == 'left':
				if self.isMoveable(dir, Map.stages[stage_num][1]):
					self.x_pos -= self.speed
				self.ani_imgs = self.left_imgs
			elif dir == 'right':
				if self.isMoveable(dir, Map.stages[stage_num][1]):
					self.x_pos += self.speed
				self.ani_imgs = self.right_imgs
			elif dir == 'up':
				if self.isMoveable(dir, Map.stages[stage_num][1]):
					self.y_pos -= self.speed
				self.ani_imgs = self.up_imgs
			elif dir == 'down':
				if self.isMoveable(dir, Map.stages[stage_num][1]):
					self.y_pos += self.speed
				self.ani_imgs = self.down_imgs
		if self.x_pos < Screen.margin // 2:
			self.x_pos = Screen.margin // 2
		if self.y_pos < Screen.margin // 2:
			self.y_pos = Screen.margin // 2
		if self.x_pos > Screen.width - 40 + Screen.margin // 2:
			self.x_pos = Screen.width - 40 + Screen.margin // 2
		if self.y_pos > Screen.height - 40 + Screen.margin // 2:
			self.y_pos = Screen.height - 40 + Screen.margin // 2

	def default_character_state(self, stage_num):
		self.img_idx = 0
		self.x_pos = 0
		self.y_pos = 0
		self.speed = 3
		self.max_bomb = 1
		self.bomb_len = 2
		self.bubble_state = False
		self.bubble_idx = 0
		self.die_state = False

	def move_correction(self, x, y, dir, cor_dir):
		if dir == 'left' or dir == 'right':
			if cor_dir == 'down': # 좌/우 무빙 아래로 보정
				# while self.y_pos < y:
				if self.y_pos < y:
					self.y_pos += self.speed
			elif cor_dir == 'up':
				# while self.y_pos > y:
				if self.y_pos > y:
					self.y_pos -= self.speed
		elif dir == 'up' or dir == 'down':
			if cor_dir == 'right': # 위 아래 무빙 오른쪽 보정
				print(self.x_pos)
				print(x)
				# while self.x_pos + 45 <= x:
				if self.x_pos + 45 <= x:
					self.x_pos += self.speed
			elif cor_dir == 'left': # 위 아래 무빙 왼쪽 보정
				# while self.x_pos > x:
				print('self x pos : ', end='')
				print(self.x_pos)
				print('x : ', end='')
				print(x)
				if self.x_pos > x:
					print('up left if')
					self.x_pos -= self.speed

	def isMoveable(self, dir, blocks):
		half_margin = Screen.margin // 2
		cur_rect = (
			self.x_pos - half_margin, self.y_pos + 10 - half_margin,
			self.x_pos + 39 - half_margin, self.y_pos + 10 + 32 - half_margin
			)
		left_x = (cur_rect[0] - 1) // 40
		left_y = ((cur_rect[1] + cur_rect[3]) // 2) // 40
		right_x = (cur_rect[2] + 1) // 40
		right_y = ((cur_rect[1] + cur_rect[3]) // 2) // 40
		up_x = ((cur_rect[0] + cur_rect[2]) // 2) // 40
		up_y = (cur_rect[1] - 1) // 40
		down_x = ((cur_rect[0] + cur_rect[2]) // 2) // 40
		down_y = (cur_rect[3] + 1) // 40
		# center_x = (cur_rect[0] + cur_rect[2]) // 2 // 40
		# center_y = (cur_rect[1] + cur_rect[3]) // 2 // 40
		center_x = round(self.center_x - 0.44) // 40
		center_y = round(self.center_y - 0.38) // 40
		if dir == 'left' or dir == 'right':
			if dir == 'left':
				# if cur_rect[0] >= half_margin - 1 and left_x < 15:
				# 	print("left x : %d | left y : %d | block : %d" %(left_x, left_y, blocks[left_y][left_x]))
				if center_x > 0 and blocks[center_y][center_x] == 10:
					print('center x : %d | center y : %d' %(center_x, center_y))
					if left_x == center_x - 1 and blocks[left_y][left_x] > -1:
						return False
					elif left_x == 0 and center_x == 0:
						return True
					else:
						return True
				elif cur_rect[0] + half_margin <= half_margin - 1 or left_x >= 15:
					return False
				elif blocks[left_y][left_x] > -1:
					return False
				elif (self.y_pos + 22) // 40 <= 12 and (self.y_pos - 22)//40 >= 0:
					if blocks[(self.y_pos + 22)//40][(self.x_pos - 22)//40] > -1:
						self.move_correction(down_x * 40, (down_y - 1) * 40 + 15, 'left', 'up') # 윗보정 좌측 아래 확인
						return True
					elif blocks[(self.y_pos - 22)//40][(self.x_pos - 22)//40] > -1:
						self.move_correction(up_x * 40, (up_y) * 40, 'left', 'down')
						return True
					return True
			if dir == 'right': # 오른 키 보정
				# if cur_rect[2] + half_margin <= half_margin + Screen.width and right_x < 15:
				# 	print("right x : %d | right y : %d | block : %d" %(right_x, right_y, blocks[right_y][right_x]))
				if center_x < 14 and blocks[center_y][center_x] == 10:
					if right_x == center_x + 1 and blocks[right_y][right_x] > -1:
						return False
					else:
						return True
				elif cur_rect[2] >= half_margin + Screen.width or right_x >= 15:
					return False
				elif blocks[right_y][right_x] > -1:
					return False
				elif (self.y_pos + 22) // 40 <= 12 and self.y_pos >= 22:
					if blocks[(self.y_pos + 22)//40][(self.x_pos + 22)//40] > -1: # 윗보정 - 우측 아래 블럭 확인
						self.move_correction(down_x * 40, (down_y - 1) * 40 + 13, 'right', 'up') # 윗보정
						return True
					elif blocks[(self.y_pos - 22)//40][(self.x_pos + 22)//40] > -1: # 아랫보정 - 우측 위 블럭 확인
						self.move_correction(up_x * 40, (center_y) * 40 + 13, 'right', 'down')
						return True
					return True
		elif dir == 'up' or dir == 'down':
			if dir == 'up':
				# if cur_rect[1] + half_margin >= half_margin - 1 and up_y < 13:
				# 	print("up x : %d | up y : %d | block : %d" %(up_x, up_y, blocks[up_y][up_x]))
				if center_y > 0 and blocks[center_y][center_x] == 10:
					if up_y == center_y - 1 and blocks[up_y][up_x] > -1:
						return False
					else:
						return True
				elif cur_rect[1] + half_margin <= half_margin - 1 or up_y >= 13:
					return False
				elif blocks[up_y][up_x] > -1:
					return False
				elif self.y_pos >= 22 and self.x_pos - 21 >= 0 and (self.x_pos + 21) // 40 <= 14:
					if blocks[(self.y_pos - 22)//40][(self.x_pos - 21)//40] > -1: # 오른보정 - 왼쪽 윗 블럭 확인
						self.move_correction((center_x + 1) * 40 + 20, self.y_pos, 'up', 'right') # 윗보정
						return True
					elif blocks[(self.y_pos - 22)//40][(self.x_pos + 21)//40] > -1: # 왼보정 - 오른 윗 블럭 확인
						self.move_correction(center_x * 40 + 20, self.y_pos, 'up', 'left')
						return True
					return True
			if dir == 'down':
				# if cur_rect[3] + half_margin <= half_margin + Screen.width and down_y < 13:
				# 	print("down x : %d | down y : %d | block : %d" %(down_x, down_y, blocks[down_y][down_x]))
				if center_y < 12 and blocks[center_y][center_x] == 10:
					if down_y == center_y + 1 and blocks[down_y][down_x] > -1:
						return False
					else:
						return True
				elif cur_rect[3] + half_margin >= half_margin + Screen.width or down_y >= 13:
					return False
				elif blocks[down_y][down_x] > -1:
					return False
				elif self.y_pos >= 22 and self.x_pos - 21 >= 0 and (self.x_pos + 21) // 40 <= 14:
					if blocks[(self.y_pos + 22)//40][(self.x_pos - 21)//40] > -1: # 오른보정 - 왼쪽 아래 블럭 확인
						self.move_correction((center_x + 1) * 40 + 20, self.y_pos, 'up', 'right') # 윗보정
						return True
					elif blocks[(self.y_pos + 22)//40][(self.x_pos + 21)//40] > -1: # 왼보정 - 오른쪽 아래 블럭 확인
						self.move_correction(center_x * 40 + 20, self.y_pos, 'up', 'left')
						return True
		return True

	def balloon_pos(self):
		half_margin = Screen.margin // 2
		cur_rect = (
			self.x_pos - half_margin, self.y_pos + 10 - half_margin,
			self.x_pos + 39 - half_margin, self.y_pos + 18 + 32 - half_margin
			)
		self.center_x = (cur_rect[0] + cur_rect[2]) / 2
		self.center_y = (cur_rect[1] + cur_rect[3]) / 2
		return (round(self.center_x / 40 - 0.44) * 40 + half_margin, (round(self.center_y / 40 - 0.38)) * 40 + half_margin)