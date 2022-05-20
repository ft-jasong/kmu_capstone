from spritesheet import Spritesheet

class Soilder(object):
	def __init__(self, img_path):
		self.spritesheet = Spritesheet(img_path)
		self.move_imgs = []
		self.die_imgs = []
		self.img_idx = 0
		self.init_imgs()
	
	def init_imgs(self):
		# move image init
		self.move_imgs.append(self.spritesheet.image_at((3, 41, 36, 36), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((47, 40, 35, 37), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((94, 40, 35, 36), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((140, 40, 37, 36), colorkey=-1))
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
		# if int(self.img_idx) % len(imgs) == 3 or int (self.img_idx) % 6 == 4:
		# 	self.y_pos -= 3
		# elif int(self.img_idx % len(imgs)) == 5:
		# 	self.y_pos += 6
		if self.img_idx % len(imgs) == 0:
			self.y_pos -= 76
		img = imgs[int(self.img_idx) % len(imgs)]
		return img
