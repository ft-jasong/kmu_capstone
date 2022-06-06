import pygame
'''from image import image_colorkey, image_info'''
from spritesheet import Spritesheet
import os.path

class Item(object):
	def __init__(self):
		self.pirate_item = Pirate_Item()

class Pirate_Item(object):
	def __init__(self):
		self.cur_path = os.path.dirname(__file__)
		self.item_path = self.cur_path + '/../asset/item/'
		self.items = []
		# '''
		# 0 = 물풍선, 1 = 신발, 2 = 물줄기, 3 = 보라풍선 
		# '''
		self.init_items()

	def init_items(self):
		item_blueballoon_sprite = Spritesheet(self.item_path + 'item.bmp')
		item_speedwalk_sprite = Spritesheet(self.item_path + 'item.bmp')
		item_waterpower_sprite = Spritesheet(self.item_path + 'item.bmp')
		item_purpleballoon_sprite = Spritesheet(self.item_path + 'item.bmp')
		item_blueballoon = (item_waterpower_sprite.image_at((80, 0, 38, 49), colorkey=-1))
		item_blueballoon = pygame.transform.scale(item_blueballoon,(40, 40))
		item_speedwalk = (item_blueballoon_sprite.image_at((81, 51, 39, 48), colorkey=-1))
		item_speedwalk = pygame.transform.scale(item_speedwalk,(40, 40))
		item_waterpower = (item_purpleballoon_sprite.image_at((83, 101, 37, 47), colorkey=-1))
		item_waterpower = pygame.transform.scale(item_waterpower,(40, 40))
		item_purpleballoon = (item_speedwalk_sprite.image_at((80, 151, 39, 49), colorkey=-1))
		item_purpleballoon = pygame.transform.scale(item_purpleballoon,(40, 40))
		self.items.append(item_blueballoon) # NUM 0
		self.items.append(item_speedwalk) # NUM 1
		self.items.append(item_waterpower) # NUM 2
		self.items.append(item_purpleballoon) # NUM 3

""""
cur_path = os.path.dirname(__file__)
img_path = cur_path + '/../asset/item/'

class Item2():
	def __init__(self):
		self.length = 2
		self.item_imgs = []
		self.item_shadow = None
		self.item_imgs_info = []
		self.init_item_imgs()
		
		# for animation
		self.img_idx = 0

	def init_item_imgs(self):
		item1_img = pygame.image.load(img_path + 'item_gloves.png')
		self.item_imgs.append(image_colorkey(item1_img, (0, 0, 40, 40), -1))
		self.item_imgs_info.append((40, 40))
		item2_img = pygame.image.load(img_path + 'item_purpleballoon-removebg-preview.png')
		self.item_imgs.append(image_colorkey(item2_img, (0, 0, 40, 40), -1))
		self.item_imgs_info.append((40, 40))
		item1_img = pygame.image.load(img_path + 'item_gloves.png')
		self.item_imgs.append(image_colorkey(item1_img, (0, 0, 40, 40), -1))
		item3_img = pygame.image.load(img_path + 'blueballoon.png')
		self.item_imgs.append(image_colorkey(item3_img, (0, 10, 50, 40), -1)) # bomb3 image가 10 * 10만큼 더 큼
		self.item_imgs_info.append((50, 40))
		item_shadow = pygame.image.load(img_path + 'bomb4.png')
		self.item_shadow = image_colorkey(item_shadow, (0, 0, 40, 40), -1)

	def animation(self, imgs, speed):
		if imgs == None:
			return self.item_imgs[0]
		self.img_idx += speed
		img = imgs[int(self.img_idx % len(self.item_imgs))]
		return img
"""