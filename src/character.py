import pygame
import spritesheet as ss
import os.path

class CharacterAnimation(object):
	def __init__(self, rel_path):
		self.cur_dir = os.path.dirname(__file__)
		self.img_path = self.cur_dir + '/' + rel_path
		self.sprite_img = ss.Spritesheet(self.img_path)
		self.up_imgs = []
		self.down_imgs = []
		self.left_imgs = []
		self.right_imgs = []
		self.img_idx = 0
		self.init_all_imgs()

	def init_up_imgs(self):
		self.up_imgs.append(self.sprite_img.image_at((438, 1, 44, 56), colorkey= -1))
		self.up_imgs.append(self.sprite_img.image_at((587, 59, 44, 55), colorkey= -1))
		self.up_imgs.append(self.sprite_img.image_at((498, 59, 43, 56), colorkey= -1))
		self.up_imgs.append(self.sprite_img.image_at((438, 1, 44, 56), colorkey= -1))
		self.up_imgs.append(self.sprite_img.image_at((618, 1, 44, 55), colorkey= -1))
		self.up_imgs.append(self.sprite_img.image_at((529, 1, 43, 56), colorkey= -1))

	def init_down_imgs(self):
		self.down_imgs.append(self.sprite_img.image_at((305, 1, 42, 57), colorkey= - 1))
		self.down_imgs.append(self.sprite_img.image_at((392, 1, 44, 56), colorkey= - 1))
		self.down_imgs.append(self.sprite_img.image_at((664, 1, 42, 55), colorkey= - 1))
		self.down_imgs.append(self.sprite_img.image_at((320, 60, 42, 57), colorkey= - 1))
		self.down_imgs.append(self.sprite_img.image_at((392, 1, 44, 56), colorkey= - 1))
		self.down_imgs.append(self.sprite_img.image_at((633, 58, 44, 56), colorkey= - 1))

	def init_left_imgs(self):
		self.left_imgs = [pygame.transform.flip(img, True, False) for img in self.right_imgs]

	def init_right_imgs(self):
		self.right_imgs.append(self.sprite_img.image_at((262, 1, 41, 58), colorkey= - 1))
		self.right_imgs.append(self.sprite_img.image_at((574, 1, 41, 57), colorkey= - 1))
		self.right_imgs.append(self.sprite_img.image_at((484, 1, 43, 56), colorkey= - 1))
		self.right_imgs.append(self.sprite_img.image_at((274, 61, 44, 57), colorkey= - 1))
		self.right_imgs.append(self.sprite_img.image_at((484, 1, 43, 56), colorkey= - 1))
		self.right_imgs.append(self.sprite_img.image_at((364, 60, 41, 57), colorkey= - 1))

	def init_all_imgs(self):
		self.init_up_imgs()
		self.init_right_imgs()
		self.init_down_imgs()
		self.init_left_imgs()

	def animation(self, imgs, speed):
		if imgs == None:
			return self.down_imgs[0]
		self.img_idx += speed
		character_img = imgs[int(self.img_idx % 6)]
		return character_img