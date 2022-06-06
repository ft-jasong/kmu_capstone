from spritesheet import Spritesheet
from screen import Screen
from random import randrange
from gameMap import *

class Soilder(object):
	def __init__(self, img_path, x_pos = 0, y_pos = 0):
		self.spritesheet = Spritesheet(img_path)
		self.move_imgs = []
		self.die_imgs = []
		self.img_idx = 0
		self.x_pos = Screen.margin // 2 + x_pos
		self.y_pos = Screen.margin // 2 + y_pos
		self.speed = 4
		self.dir = 'down'
		self.init_imgs()
		self.rect = self.move_imgs[0].get_rect()
		self.dir_time = 0
	
	def init_imgs(self):
		# move image init
		self.move_imgs.append(pygame.transform.scale(self.spritesheet.image_at((3, 41, 36, 36), colorkey=-1), (37, 37)))
		self.move_imgs.append(pygame.transform.scale(self.spritesheet.image_at((47, 40, 35, 37), colorkey=-1), (37, 37)))
		self.move_imgs.append(pygame.transform.scale(self.spritesheet.image_at((94, 40, 35, 36), colorkey=-1), (37, 37)))
		self.move_imgs.append(pygame.transform.scale(self.spritesheet.image_at((140, 40, 37, 36), colorkey=-1), (37, 37)))
		# die image init
		self.die_imgs.append(self.spritesheet.image_at((3, 121, 41, 32), colorkey=-1))
		self.die_imgs.append(self.spritesheet.image_at((51, 121, 38, 33), colorkey=-1))
		self.die_imgs.append(self.spritesheet.image_at((100, 119, 34, 37), colorkey=-1))
		self.die_imgs.append(self.spritesheet.image_at((147, 128, 45, 27), colorkey=-1))

	def animation(self, imgs, speed):
		if imgs == None:
			return self.move_imgs[0]
		self.img_idx += speed
		img = imgs[int(self.img_idx) % len(imgs)]
		return img
	
	def check_up_move(self, stage_num):
		x = (self.x_pos - Screen.margin // 2)
		y = (self.y_pos - Screen.margin // 2)
		if 0 <= (y - 1) // 40 <= 12 and Map.stages[stage_num][1][(y - 1) // 40][x // 40] == -1:
			return True
		else:
			return False
	
	def check_down_move(self, stage_num):
		x = (self.x_pos - Screen.margin // 2)
		y = (self.y_pos - Screen.margin // 2)
		if 0 <= (y + 1 + 40) // 40 <= 12 and Map.stages[stage_num][1][(y + 1 + 37) // 40][x // 40] == -1:
			return True
		else:
			return False
	
	def check_left_move(self, stage_num):
		x = (self.x_pos - Screen.margin // 2)
		y = (self.y_pos - Screen.margin // 2)
		if 0 <= (x - 1) // 40 <= 14 and Map.stages[stage_num][1][y // 40][(x - 1) // 40] == -1:
			return True
		else:
			return False
	
	def check_right_move(self, stage_num):
		x = (self.x_pos - Screen.margin // 2)
		y = (self.y_pos - Screen.margin // 2)
		if 0 <= (x + 1 + 40) // 40 <= 14 and Map.stages[stage_num][1][y // 40][(x + 1 + 37) // 40] == -1:
			return True
		else:
			return False

	def search_valid_move(self, stage_num):
		x = (self.x_pos - Screen.margin // 2)
		y = (self.y_pos - Screen.margin // 2)
		rand_dir = randrange(0,4)
		print(rand_dir)
		dir = ['right', 'up', 'left', 'down']
		if rand_dir == 0 and self.check_right_move(stage_num) == True:
			return 'right'
		elif rand_dir == 1 and self.check_up_move(stage_num) == True:
			return 'up'
		elif rand_dir == 2 and self.check_left_move(stage_num) == True:
			return 'left'
		elif rand_dir == 3 and self.check_down_move(stage_num) == True:
			return 'down'
		return dir[rand_dir]

	def move(self, stage_num):
		if self.y_pos >= Screen.margin // 2 and self.x_pos >= Screen.margin // 2:
			x = (self.x_pos - Screen.margin // 2)
			y = (self.y_pos - Screen.margin // 2)
			self.dir_time += 1
			if self.dir == 'left':
				if (x - 1) // 40 == -1 or Map.stages[stage_num][1][y // 40][(x - 1) // 40] != -1:
					self.dir = self.search_valid_move(stage_num)
				else:
					self.x_pos -= self.speed
			if self.dir == 'right':
				if (x + 1) // 40 > 13 or Map.stages[stage_num][1][y // 40][(x + 1 + 37) // 40] != -1:
					print('right serach move')
					self.dir = self.search_valid_move(stage_num)
				else:
					self.x_pos += self.speed
			if self.dir == 'up':
				if (y - 1) // 40 == -1 or Map.stages[stage_num][1][(y - 1) // 40][x // 40] != -1:
					self.dir = self.search_valid_move(stage_num)
				else:
					self.y_pos -= self.speed
			if self.dir == 'down':
				if (y + 1) // 40 > 11 or Map.stages[stage_num][1][(y + 1 + 37) // 40][x // 40] != -1:
					print('soilder dir down')
					self.dir = self.search_valid_move(stage_num)
				else:
					self.y_pos += self.speed
			if self.dir_time > 200:
				self.dir_time = 0
				self.dir = self.search_valid_move(stage_num)
			if self.dir == None:
					self.dir = self.search_valid_move(stage_num)

class Boss(object):
	def __init__(self, img_path):
		self.spritesheet = Spritesheet(img_path)
		self.move_imgs = []
		self.attack_imgs = []
		self.hit_img = self.spritesheet.image_at((1, 1, 1, 1), colorkey=-1)
		self.die_imgs = []
		self.img_idx = 0
		self.x_pos = 200
		self.y_pos = 200
		self.init_imgs()

	def init_imgs(self):
		# move img init
		self.move_imgs.append(self.spritesheet.image_at((5, 145, 119, 110), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((134, 150, 120, 105), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((271, 152, 118, 102), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((415, 130, 118, 125), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((551, 129, 118, 125), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((5, 269, 118, 125), colorkey=-1))
		# attack img init
		self.attack_imgs.append(self.spritesheet.image_at((5, 586, 118, 102), colorkey=-1))
		self.attack_imgs.append(self.spritesheet.image_at((151, 563, 118, 125), colorkey=-1))
		self.attack_imgs.append(self.spritesheet.image_at((302, 559, 118, 125), colorkey=-1))
		self.attack_imgs.append(self.spritesheet.image_at((443, 560, 118, 125), colorkey=-1))
		self.attack_imgs.append(self.spritesheet.image_at((588, 578, 120, 105), colorkey=-1))
		# hit image init
		self.hit_img = self.spritesheet.image_at((7, 407, 118, 140), colorkey=-1)
		# die image init
		self.die_imgs.append(self.spritesheet.image_at((14, 1055, 120, 140), colorkey=-1))
		self.die_imgs.append(self.spritesheet.image_at((159, 1138, 166, 64), colorkey=-1))
		self.die_imgs.append(self.spritesheet.image_at((353, 1140, 175, 62), colorkey=-1))
		self.die_imgs.append(self.spritesheet.image_at((561, 1137, 183, 61), colorkey=-1))
		self.die_imgs.append(self.spritesheet.image_at((10, 1254, 159, 61), colorkey=-1))
		self.die_imgs.append(self.spritesheet.image_at((200, 1251, 179, 61), colorkey=-1))


	def animation(self, imgs, speed):
		if imgs == None:
			return self.move_imgs[0]
		self.img_idx += speed
		img = imgs[int(self.img_idx) % len(imgs)]
		return img
