import spritesheet as ss
import pygame

class Soilder(object):
	def __init__(self, img_path):
		self.spritesheet = ss.Spritesheet(img_path)
		self.move_imgs = []
		self.img_idx = 0
		self.init_imgs()
	
	def init_imgs(self):
		self.imgs.append(self.spritesheet.image_at((), colorkey=-1))
		self.imgs.append(self.spritesheet.image_at((), colorkey=-1))
		self.imgs.append(self.spritesheet.image_at((), colorkey=-1))
		self.imgs.append(self.spritesheet.image_at((), colorkey=-1))

	def animation(self, imgs, speed):
		if imgs == None:
			return self.down_imgs[0]
		self.img_idx += speed
		img = imgs[int(self.img_idx % 6)]
		return img
		
class Boss(object):
	def __init__(self, img_path):
		self.spritesheet = ss.Spritesheet(img_path)
		self.move_imgs = []
		self.attack_imgs = []
		self.img_idx = 0
		self.init_imgs()

	def init_imgs(self):
		self.move_imgs.append(self.spritesheet.image_at((), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((), colorkey=-1))
		####################ATTACK IMGS##############################
		self.attack_imgs.append(self.spritesheet.image_at((), colorkey=-1))
		self.attack_imgs.append(self.spritesheet.image_at((), colorkey=-1))
		self.attack_imgs.append(self.spritesheet.image_at((), colorkey=-1))
		self.attack_imgs.append(self.spritesheet.image_at((), colorkey=-1))

	def animation(self, imgs, speed):
		if imgs == None:
			return self.down_imgs[0]
		self.img_idx += speed
		img = imgs[int(self.img_idx % 6)]
		return img
