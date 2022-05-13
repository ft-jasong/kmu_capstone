import pygame

class Spritesheet(object):
	def __init__(self, filename):
		try:
			self.sheet = pygame.image.load(filename).convert()
		except pygame.error as message:
			print('Unable to load spritesheet image:', filename)
			raise SystemExit(message)
	# Load a specific image from a specific rectangle
	def image_at(self, rectangle, colorkey = None):
		"Loads image from x, y, x+offset, y+offset"
		rect = pygame.Rect(rectangle)
		image = pygame.Surface(rect.size).convert()
		image.blit(self.sheet, (0, 0), rect)
		if colorkey != None:
			if colorkey == -1:
				colorkey = image.get_at((0,0))
			image.set_colorkey(colorkey, pygame.RLEACCEL)
		return image
	# Load a whole bunch of images and return them as a list
	def images_at(self, rects, colorkey = None):
		"Loads multiple images, supply a list of coordinates"
		return [self.image_at(rect, colorkey) for rect in rects]
	# Load a whole strip of images
	def load_strip(self, rect, image_count, colorkey = None):
		"Loads a strip of images and returns them as a list"
		tups = [(rect[0]+(2+rect[2])*x, rect[1], rect[2], rect[3])
				for x in range(image_count)]
		return self.images_at(tups, colorkey)

pygame.init()

class Screen(object):
	def __init__(self):
		self.width = 624
		self.height = 624

	def set_display(self):
		self.window = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption("Copy Crazy Arcade")
	
	def set_background(self, bg_path):
		self.background = pygame.load(bg_path)
		self.background = pygame.transform.scale(self.background, (self.width, self.height))

screen = Screen()
screen.set_display()
# screen.set_background("./asset/background/background.png")
board = [[0] * 13 for _ in range(13)]
clock = pygame.time.Clock()
mapx = 0
mapy = 0
tile = pygame.image.load("./asset/map/")

running = True
while running:
	dt = clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	for y in range(13):
		for x in range(13):
			screen.window.blit()
