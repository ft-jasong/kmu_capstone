from spritesheet import Spritesheet

class Soilder(object):
	def __init__(self, img_path):
		self.spritesheet = Spritesheet(img_path)
		self.move_imgs = []
		self.die_imgs = []
		self.img_idx = 0
		self.init_imgs()
	
	def init_imgs(self):
		self.move_imgs.append(self.spritesheet.image_at((3, 41, 36, 36), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((47, 40, 35, 37), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((94, 40, 35, 36), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((140, 40, 37, 36), colorkey=-1))
		##################### DIE IMGS #################################
		self.die_imgs.append(self.spritesheet.image_at((3, 121, 41, 32), colorkey=-1))
		self.die_imgs.append(self.spritesheet.image_at((51, 121, 38, 33), colorkey=-1))
		self.die_imgs.append(self.spritesheet.image_at((100, 119, 34, 37), colorkey=-1))
		self.die_imgs.append(self.spritesheet.image_at((147, 128, 45, 27), colorkey=-1))

	def animation(self, imgs, speed):
		if imgs == None:
			return self.move_imgs[0]
		self.img_idx += speed
		img = imgs[int(self.img_idx % len(imgs))]
		return img
		

class Boss(object):
	def __init__(self, img_path):
		self.spritesheet = Spritesheet(img_path)
		self.move_imgs = []
		self.attack_imgs = []
		self.hit_img = self.spritesheet.image_at((1, 1, 1, 1), colorkey=-1)
		self.die_imgs = []
		self.img_idx = 0
		self.init_imgs()

	def init_imgs(self):
		self.move_imgs.append(self.spritesheet.image_at((5, 145, 119, 110), colorkey=-1))
		self.move_imgs.append(self.spritesheet.image_at((134, 150, 120, 105), colorkey=-1))
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
		img = imgs[int(self.img_idx % len(imgs))]
		return img
