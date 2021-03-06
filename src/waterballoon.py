import pygame
from image import image_colorkey
import os.path
from gameMap import Map

cur_path = os.path.dirname(__file__)
img_path = cur_path + '/../asset/Bomb/'

class Explode():
	def __init__(self):
		self.explode_center = []
		self.explode_center_info = []
		self.explode_up = []
		self.explode_up_info = []
		self.explode_down = []
		self.explode_down_info = []
		self.explode_left = []
		self.explode_left_info = []
		self.explode_right = []
		self.explode_right_info = []
		self.explode_time = 0
		self.init_explode_imgs()
		# for animation
		self.img_idx = 0

	def init_explode_imgs(self):
		# center image init
		exp_center_img0 = pygame.image.load(img_path + 'explosion00.png').convert()
		self.explode_center.append(image_colorkey(exp_center_img0, (0, 0, 40, 40)))
		self.explode_center_info.append((40, 40))
		exp_center_img1 = pygame.image.load(img_path + 'explosion01.png').convert()
		self.explode_center.append(image_colorkey(exp_center_img1, (0, 0, 40, 40)))
		self.explode_center_info.append((40, 40))
		exp_center_img2 = pygame.image.load(img_path + 'explosion02.png').convert()
		self.explode_center.append(image_colorkey(exp_center_img2, (0, 0, 40, 40)))
		self.explode_center_info.append((40, 40))
		# up image init
		exp_up_img0 = pygame.image.load(img_path + 'explosion10.png').convert()
		self.explode_up.append(image_colorkey(exp_up_img0, (0, 0, 40, 40), -1))
		self.explode_up_info.append((40, 40))
		exp_up_img1 = pygame.image.load(img_path + 'explosion11.png').convert()
		self.explode_up.append(image_colorkey(exp_up_img1, (0, 0, 40, 40), -1))
		self.explode_up_info.append((40, 40))
		exp_up_img2 = pygame.image.load(img_path + 'explosion12.png').convert()
		self.explode_up.append(image_colorkey(exp_up_img2, (0, 0, 40, 40), -1))
		self.explode_up_info.append((40, 40))
		exp_up_img3 = pygame.image.load(img_path + 'explosion13.png').convert()
		self.explode_up.append(image_colorkey(exp_up_img3, (0, 0, 40, 40), -1))
		self.explode_up_info.append((40, 40))
		exp_up_img4 = pygame.image.load(img_path + 'explosion15.png').convert()
		self.explode_up.append(image_colorkey(exp_up_img4, (0, 0, 40, 40), -1))
		self.explode_up_info.append((40, 40))
		# down image init
		self.explode_down = [pygame.transform.rotate(img, 180) for img in self.explode_up]
		self.explode_down_info = [size for size in self.explode_up_info]
		# # left image init
		# self.explode_down
		self.explode_left = [pygame.transform.rotate(img, 90) for img in self.explode_up]
		self.explode_left_info = [size for size in self.explode_up_info]
		# # right image init
		self.explode_right = [pygame.transform.rotate(img, 270) for img in self.explode_up]
		self.explode_right_info = [size for size in self.explode_up_info]
	
	def animation(self, imgs, speed):
		if imgs == None:
			# print('waterballoon image animation imgs is NULL')
			return None
		self.img_idx += speed
		img = imgs[int(self.img_idx) % len(imgs)]
		return img


	def explode(self, length, x_pos, y_pos, stage_num):
		up_colide = True
		down_colide = True
		left_colide = True
		right_colide = True
		up_len = 0
		down_len = 0
		left_len = 0
		right_len = 0
		# print('x pos : %d | y pos : %d | len : %d' %(x_pos, y_pos, length))
		for y in range(y_pos - 1, y_pos - length, -1):
			# print('this is for up')
			if y < 0:
				break
			elif Map.stages[stage_num][1][y][x_pos] > -1:
				if up_colide is True:
					up_colide = False
				if Map.stages[stage_num][1][y][x_pos] == 1 or Map.stages[stage_num][1][y][x_pos] == 2:
					# print('up block colide')
					Map.block_colide(Map, stage_num, x_pos, y)
				break
			elif Map.stages[stage_num][1][y][x_pos] <= -80:
				# print('up item colide')
				Map.item_colide(Map, stage_num, x_pos, y)
				up_len += 1
			else:
				up_len += 1
		for y in range(y_pos + 1, y_pos + length):
			# print('stage num : %d | y : %d | x_pos : %d' %(stage_num, y, x_pos))
			if y > 12:
				break
			elif Map.stages[stage_num][1][y][x_pos] > -1:
				down_colide = False
				if Map.stages[stage_num][1][y][x_pos] == 1 or Map.stages[stage_num][1][y][x_pos] == 2:
					Map.block_colide(Map, stage_num, x_pos, y)
				break
			elif Map.stages[stage_num][1][y][x_pos] <= -80:
				Map.item_colide(Map, stage_num, x_pos, y)
				down_len += 1
			else:
				down_len += 1
		for x in range(x_pos - 1, x_pos - length, -1):
			if x < 0:
				break
			elif Map.stages[stage_num][1][y_pos][x] > -1 and left_colide is True:
				left_colide = False
				if Map.stages[stage_num][1][y_pos][x] == 1 or Map.stages[stage_num][1][y_pos][x] == 2:
					Map.block_colide(Map, stage_num, x, y_pos)
				break
			elif Map.stages[stage_num][1][y_pos][x] <= -80:
				Map.item_colide(Map, stage_num, x, y_pos)
				left_len += 1	
			else:
				left_len += 1
		for x in range(x_pos + 1, x_pos + length):
			if x > 14:
				break
			elif Map.stages[stage_num][1][y_pos][x] > -1 and right_colide is True:
				right_colide = False
				if Map.stages[stage_num][1][y_pos][x] == 1 or Map.stages[stage_num][1][y_pos][x] == 2:
					Map.block_colide(Map, stage_num, x, y_pos)
				break
			elif Map.stages[stage_num][1][y_pos][x] <= -80:
				Map.item_colide(Map, stage_num, x, y_pos)
				right_len += 1	
			else:
				right_len += 1
		return (up_len, down_len, left_len, right_len)
class Bomb():
	def __init__(self, length):
		self.length = length
		self.bomb_imgs = []
		self.bomb_shadow = None
		self.bomb_imgs_info = []
		self.init_balloon_imgs()
		# for animation
		self.img_idx = 0
		self.explode = Explode()

	def init_balloon_imgs(self):
		bomb1_img = pygame.image.load(img_path + 'bomb1.png').convert()
		self.bomb_imgs.append(image_colorkey(bomb1_img, (0, 0, 40, 40), -1))
		self.bomb_imgs_info.append((40, 40))
		bomb2_img = pygame.image.load(img_path + 'bomb2.png').convert()
		self.bomb_imgs.append(image_colorkey(bomb2_img, (0, 0, 40, 40), -1))
		self.bomb_imgs_info.append((40, 40))
		bomb1_img = pygame.image.load(img_path + 'bomb1.png').convert()
		self.bomb_imgs.append(image_colorkey(bomb1_img, (0, 0, 40, 40), -1))
		bomb3_img = pygame.image.load(img_path + 'bomb3.png').convert()
		self.bomb_imgs.append(image_colorkey(bomb3_img, (0, 10, 50, 40), -1)) # bomb3 image??? 10 * 10?????? ??? ???
		self.bomb_imgs_info.append((50, 40))
		bomb_shadow = pygame.image.load(img_path + 'bomb4.png').convert()
		self.bomb_shadow = image_colorkey(bomb_shadow, (0, 0, 40, 40), -1)

	def animation(self, imgs, speed):
		if imgs == None:
			return self.bomb_imgs[0]
		self.img_idx += speed
		img = imgs[int(self.img_idx % len(self.bomb_imgs))]
		return img