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
		self.img = self.move_imgs[0]
		self.die_idx = 0
		self.die_flag = False
		self.move_flag = True
	
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
		if self.die_flag is True:
			self.die_idx += speed
			self.img = self.die_imgs[int(self.die_idx) % 4]
			return self.img
		else:
			if imgs == None:
				return self.move_imgs[0]
			self.img_idx += speed
			self.img = imgs[int(self.img_idx) % len(imgs)]
			return self.img
	
	def check_up_move(self, stage_num):
		x = (self.x_pos - Screen.margin // 2)
		y = (self.y_pos - Screen.margin // 2)
		if 0 <= (y - 3) // 40 <= 12 and Map.stages[stage_num][1][(y - 3) // 40][x // 40] <= -1:
			return True
		else:
			return False
	
	def check_down_move(self, stage_num):
		x = (self.x_pos - Screen.margin // 2)
		y = (self.y_pos - Screen.margin // 2)
		if 0 <= (y + 3 + 40) // 40 <= 12 and Map.stages[stage_num][1][(y + 3 + 37) // 40][x // 40] <= -1:
			return True
		else:
			return False
	
	def check_left_move(self, stage_num):
		x = (self.x_pos - Screen.margin // 2)
		y = (self.y_pos - Screen.margin // 2)
		if 0 <= (x - 3) // 40 <= 14 and Map.stages[stage_num][1][y // 40][(x - 3) // 40] <= -1:
			return True
		else:
			return False
	
	def check_right_move(self, stage_num):
		x = (self.x_pos - Screen.margin // 2)
		y = (self.y_pos - Screen.margin // 2)
		if 0 <= (x + 3 + 40) // 40 <= 14 and Map.stages[stage_num][1][y // 40][(x + 3 + 40) // 40] <= -1:
			return True
		else:
			return False

	def search_valid_move(self, stage_num):
		x = (self.x_pos - Screen.margin // 2)
		y = (self.y_pos - Screen.margin // 2)
		rand_dir = randrange(0,4)
		# print(rand_dir)
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
		if self.move_flag is True:
			if self.y_pos >= Screen.margin // 2 and self.x_pos >= Screen.margin // 2:
				x = (self.x_pos - Screen.margin // 2)
				y = (self.y_pos - Screen.margin // 2)
				self.dir_time += 1
				if self.dir == 'left':
					if (x - 1) // 40 <= -1 or Map.stages[stage_num][1][y // 40][(x - 1) // 40] > -1:
						self.dir = self.search_valid_move(stage_num)
					else:
						self.x_pos -= self.speed
				if self.dir == 'right':
					if (x + 1) // 40 > 13 or Map.stages[stage_num][1][y // 40][(x + 1 + 37) // 40] > -1:
						# print('right serach move')
						self.dir = self.search_valid_move(stage_num)
					else:
						self.x_pos += self.speed
				if self.dir == 'up':
					if (y - 1) // 40 <= -1 or Map.stages[stage_num][1][(y - 1) // 40][x // 40] > -1:
						self.dir = self.search_valid_move(stage_num)
					else:
						self.y_pos -= self.speed
				if self.dir == 'down':
					if (y + 1) // 40 > 11 or Map.stages[stage_num][1][(y + 1 + 37) // 40][x // 40] > -1:
						# print('soilder dir down')
						self.dir = self.search_valid_move(stage_num)
					else:
						self.y_pos += self.speed
				# if self.dir_time > 150 and (self.x_pos - Screen.margin // 2) % 40 == 0 and (self.y_pos - Screen.margin // 2) % 40:
				# 	self.dir_time = 0
				# 	self.dir = self.search_valid_move(stage_num)
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
		self.x_pos = 240 + Screen.margin // 2
		self.y_pos = 80 +  Screen.margin // 2
		self.die_flag = False
		self.die_idx = 0
		self.health = 10
		self.move_idx = 0
		self.speed = 4
		self.move_flag = True
		self.dir = 'down'
		self.dirs = ['left', 'right', 'up', 'down']
		self.dir_time = 0
		self.img = None
		self.init_imgs()
		self.rect = self.img.get_rect()
		self.size = self.rect.size
		self.blit_x = 0
		self.blit_y = 0
		self.state = 'move' # 'attack' 'hit'
		self.states = ['move', 'attack', 'hit']
		self.attack_idx = 0
		self.past_state = 'move'
		self.hit_time = 0

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
		
		self.img = self.move_imgs[0]
	
	def random_state(self):
		rand_idx = randrange(0, 2)
		# print('rand idx', end='')
		# print(rand_idx)
		self.state = self.states[rand_idx]

	def move(self):
		if self.health <= 0:
			self.die_flag = True
		elif self.state == 'move':
			self.rect = self.img.get_rect()
			self.rect.top = self.y_pos
			self.rect.left = self.x_pos
			if self.move_idx == 0:
				self.dir = self.dirs[randrange(0, 4)]
			if self.dir == 'left':
				if self.x_pos > Screen.margin // 2:
					self.x_pos -= self.speed
			elif self.dir == 'right':
				if self.x_pos + self.size[0] < Screen.margin // 2 + Screen.width:
					self.x_pos += self.speed
			elif self.dir == 'down':
				if self.y_pos + self.size[1] < Screen.margin // 2 + Screen.height:
					self.y_pos += self.speed
			elif self.dir == 'up':
				if self.y_pos > Screen.margin // 2:
					self.y_pos -= self.speed
			elif dir == None:
				self.img = self.move_imgs[0]
			self.move_idx += 0.1
			self.img = self.move_imgs[int(self.move_idx) % 6]
			if 3 <= int(self.move_idx) % 6 <= 4:
				self.blit_y -= 3
			elif int(self.move_idx) % 6 == 5:
				self.blit_y += 6
			if self.move_idx >= 6:
				self.move_idx = 0
				self.blit_y = 0
				self.random_state()
		elif self.state == 'hit':
			self.hit()

	def summon_soilder(self, soilder_num): # 얘가 move 보다 먼저 나와야함 그래야 state 안꼬임
		if self.health > 0 and self.state == 'attack':
			rand_x = randrange(0, 15)
			rand_y = randrange(0, 13)
			if self.attack_idx == 0 and soilder_num < 3:
				self.img = self.attack_imgs[int(self.attack_idx) % 6]
				self.attack_idx += 0.1
				return (rand_x * 40, rand_y * 40)
			elif self.attack_idx < 5:
				self.img = self.attack_imgs[int(self.attack_idx) % 6]
				self.attack_idx += 0.05
				return None
			else:
				self.state = 'move'
				self.attack_idx = 0
				return None
		elif self.state == 'hit':
			self.attack_idx = 0
			self.hit()
			return None
		else:
			# self.state = 'move'
			# self.attack_idx = 0
			return None
	def die_animation(self):
		self.die_idx += 0.05
		self.img = self.die_imgs[int(self.die_idx) % 4]

	def hit(self):
		if self.hit_time == 0:
			self.health -= 1
			if self.health <= 0:
				return None
			self.past_state = self.state
			self.state = 'hit'
		self.img = self.hit_img
		self.hit_time += 0.1
		if self.hit_time > 10:
			self.state = self.past_state
			self.hit_time = 0
			
	def animation(self, imgs, speed):
		if self.die_flag is True:
			self.die_idx += speed
			self.img = self.die_imgs[int(self.die_idx) % 6]
			return self.img
		else:
			if imgs == None:
				return self.move_imgs[0]
			self.img_idx += speed
			self.img = imgs[int(self.img_idx) % len(imgs)]
			return self.img
