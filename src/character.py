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

	def init_all_imgs(self):
		self.init_up_imgs()
		self.init_right_imgs()
		self.init_down_imgs()
		self.init_left_imgs()
		self.init_stop_imgs()
		self.ani_imgs = self.down_imgs

	def __init__(self, rel_path):
		self.cur_dir = os.path.dirname(__file__)
		self.img_path = self.cur_dir + '/' + rel_path
		self.sprite_img = ss.Spritesheet(self.img_path)
		self.up_imgs = []
		self.down_imgs = []
		self.left_imgs = []
		self.right_imgs = []
		self.ani_imgs = []
		self.img_idx = 0
		self.x_pos = Screen.margin // 2
		self.y_pos = Screen.margin // 2
		self.speed = 5
		self.move_flag = False
		self.left_stop = None
		self.right_stop = None
		self.up_stop = None
		self.down_stop = None
		self.init_all_imgs()

	def animation(self, speed, dir):
		if self.move_flag == True:
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

	# def check_available_move(self, stage_num):
	# 	move_box = (
	# 		self.x_pos + 21, self.y_pos + 28,
	# 		self.x_pos + 61, self.y_pos + 68
	# 		)
	# 	stage = Map.stages[stage_num]
	# 	for y in range(15):
	# 		for x in range(13):
	# 			if isMoveable(move_box, x, y):
	# 				return True

	def move_position(self, dir, stage_num):
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

	def default_character_state(self):
		self.img_idx = 0
		self.x_pos = 0
		self.y_pos = 0
		self.speed = 3

	def move_correction(self, x, y, dir):
		if dir == 'left' or dir == 'right':
			if y > self.y_pos:
				while self.y_pos < y:
					self.y_pos += self.speed
			else:
				while self.y_pos > y:
					self.y_pos -= self.speed
		elif dir == 'up' or dir == 'down':
			if x > self.x_pos:
				while self.x_pos < x:
					self.x_pos += self.speed
			else:
				while self.x_pos > x:
					self.x_pos -= self.speed

	def isMoveable(self, dir, blocks):
		# center_x = self.x_pos + 20 + 20
		# center_y = self.y_pos + 30 + 20
		# div_x = self.x_pos // 40
		# div_y = self.y_pos // 40
		cur_rect = (self.x_pos, self.y_pos, self.x_pos + 39, self.y_pos + 39)
		# if div_x > 14:
		# 	div_x = 14
		# if div_y > 12:
		# 	div_y = 12
		# if div_x == 0:
		# 	x_percent = int((40 + 20) / center_x)
		# else:
		# 	x_percent = int(center_x / div_x * 100)
		# if div_y == 0:
		# 	y_percent = int((40 + 20) / center_x)
		# else:
		# 	y_percent = int(center_y / div_y * 100)
		# print('div_x : ' + (str)(div_x) + ' div_y ' + (str)(div_y))
		# print('end_x : ' + (str)(end_x) + ' end_y ' + (str)(end_y))
		# print(blocks[div_y][div_x])
		for idx, pos in enumerate(cur_rect):
			print('idx' + str(idx))
			print((pos - 20) // 40)
		if dir == 'left' or dir == 'right':
			if dir == 'left':
				if cur_rect[0] <= Screen.margin // 2:
					return False
				elif blocks[(cur_rect[1] - Screen.margin) // 40][((cur_rect[0] - Screen.margin // 2) - 1) // 40] != -1:
					return False
				else:
					return True
			if dir == 'right':
				if cur_rect[2] >= Screen.margin // 2 + Screen.width:
					return False
				elif blocks[(cur_rect[1] - Screen.margin) // 40][((cur_rect[2] - Screen.margin // 2) + 2) // 40] != -1:
					return False
				else:
					return True
		return True
		# 	elif dir == 'right':
		# 		if end_x >= Screen.width + Screen.margin // 2:
		# 			return False
		# 		elif (end_x - 20) // 40 > 14:
		# 			return False
		# 		elif blocks[div_y][(end_x - 20) // 40] != -1:
		# 			print('end_x')
		# 			print((end_x - 20) // 40)
		# 			return False
		# 		else:
		# 			return True
		# elif dir == 'up' or dir == 'down' and 0 < div_y < 12:
		# 	if dir == 'up':
		# 		if end_y == Screen.margin // 2:
		# 			return False
		# 		elif end_y // 40 == 0:
		# 			return False
		# 		elif blocks[start_y // 40 - 1][div_x] != -1:
		# 			return False
		# 		else:
		# 			return True
		# 	elif dir == 'down':
		# 		if end_y >= Screen.width + Screen.margin // 2:
		# 			return False
		# 		elif end_y // 40 >= 12:
		# 			return False
		# 		elif blocks[end_y // 40 + 1][div_x] != -1:
		# 			return False
		# 		else:
		# 			return True

		# if dir == 'left':
		# 	if 0 < div_x < 14 and 0 < div_y < 12:
		# 		if y_percent >= 75:
		# 			if blocks[div_y - 1][div_x] != -1 and blocks[div_y - 1][div_x + 1] == -1:
		# 				self.move_correction(div_x * 40 + 20, (div_y + 1) * 40 + 20, dir)
		# 				return True
		# 		elif y_percent <= 25:
		# 			if blocks[div_y - 1][div_x] != -1 and blocks[div_y - 1][div_x - 1] == -1:
		# 				self.move_correction(div_x * 40 + 20, (div_y - 1) * 40 + 20, dir)
		# 				return True
		# 		else:
		# 			if blocks[div_y - 1][div_x] == -1:
		# 				# self.move_correction(div_x * 40 + 20, div_y * 40 + 20, dir)
		# 				return True
		# 			else:
		# 				return False
		# 	return True
		# elif dir == 'right':
		# 	if 0 < div_x < 14 and 0 < div_y < 12:
		# 		if y_percent >= 75:
		# 			if blocks[div_y + 1][div_x] != -1 and blocks[div_y + 1][div_x + 1] == -1:
		# 				self.move_correction(div_x * 40 + 20, (div_y + 1) * 40 + 20, dir)
		# 				return True
		# 		elif y_percent <= 25:
		# 			if blocks[div_y + 1][div_x] != -1 and blocks[div_y + 1][div_x - 1] == -1:
		# 				self.move_correction(div_x * 40 + 20, (div_y - 1) * 40 + 20, dir)
		# 				return True
		# 		else:
		# 			if blocks[div_y + 1][div_x] == -1:
		# 				# self.move_correction(div_x * 40 + 20, div_y * 40 + 20, dir)
		# 				return True
		# 			else:
		# 				return False
		# 	return True
		# elif dir == 'up':
		# 	if 0 < div_x < 14 and 0 < div_y < 12:
		# 		if x_percent >= 75:
		# 			if blocks[div_y][div_x] != -1 and blocks[div_y + 1][div_x - 1] == -1:
		# 				self.move_correction((div_x + 1) * 40 + 20, div_y * 40 + 20, dir)
		# 				return True
		# 		elif x_percent <= 25:
		# 			if blocks[div_y][div_x] != -1 and blocks[div_y - 1][div_x - 1] == -1:
		# 				self.move_correction((div_x - 1)* 40 + 20, div_y * 40 + 20, dir)
		# 				return True
		# 		else:
		# 			if blocks[div_y][div_x - 1] == -1:
		# 				# self.move_correction(div_x * 40 + 20, div_y * 40 + 20, dir)
		# 				return True
		# 			else:
		# 				return False
		# 	return True
		# elif dir == 'down':
		# 	if 0 < div_x < 14 and 0 < div_y < 12:
		# 		if x_percent >= 75:
		# 			if blocks[div_y][div_x] != -1 and blocks[div_y + 1][div_x] == -1:
		# 				self.move_correction((div_x + 1) * 40, div_y * 40, dir)
		# 				return True
		# 		elif x_percent <= 25:
		# 			if blocks[div_y][div_x] != -1 and blocks[div_y - 1][div_x] == -1:
		# 				self.move_correction((div_x - 1)* 40, div_y * 40, dir)
		# 				return True
		# 		else:
		# 			if blocks[div_y][div_x + 1] == -1:
		# 				# self.move_correction(div_x * 40, div_y * 40, dir)
		# 				return True
		# 			else:
		# 				return False
		# 	return True
		return True # for test

	def balloon_pos(self):
		center_x = self.x_pos + 26
		center_y = self.y_pos + 40
		return (round(center_x / 40 - 1) * 40 + 20, round(center_y / 40 - 1) * 40 + 20)