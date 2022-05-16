import pygame
import spritesheet as ss
import os.path

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

class Tile(object):
	def __init__(self, tile_path):
		self.ss = ss.Spritesheet(tile_path)
		self.tiles = self.ss.load_strip((0, 0, 40, 40), 13, colorkey=None)
		for i in range(len(self.tiles)):
			self.tiles[i] = pygame.transform.scale(self.tiles[i], (48, 48))
		self.img = self.tiles[0]

pygame.init()

screen = Screen()
screen.set_display()
board = [[0] * 13 for _ in range(13)]
clock = pygame.time.Clock()
cur_path = os.path.dirname(__file__)
asset_path = cur_path + '/../asset/'

tile = Tile(asset_path + 'map/map_camp_tile2.png')
# tile.resize_tile()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	for y in range(13):
		for x in range(13):
			screen.window.blit(tile.tiles[x], (x * 48, y * 48))
	pygame.display.update()
pygame.quit()