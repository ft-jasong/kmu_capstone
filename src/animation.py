class ListAnimation():
	def __init__(self):
		self.img_idx = 0

	def animation(self, imgs, speed):
		if imgs == None:
			return None
		self.img_idx += speed
		character_img = imgs[int(self.img_idx % 6)]
		return character_img