import pygame
from animation import CharacterAnimation
import spritesheet as ss
import os.path

class Screen(object):
	def __init__(self):
		self.width = 624
		self.height = 624

	def set_display(self):
		self.window = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption("Copy Crazy Arcade")

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

# for img test #

# character_ss = ss.Spritesheet(asset_path + 'character/animation.png')
Character = CharacterAnimation('../asset/character/animation.png')
img = Character.down_imgs[0]
dir = None
x_speed = 0
y_speed = 0
x_pos = 0
y_pos = 0
# test finished

tile = Tile(asset_path + 'map/map_camp_tile2.png')
# tile.resize_tile()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				dir = Character.left_imgs
				x_speed = -3
				y_speed = 0
			elif event.key == pygame.K_RIGHT:
				dir = Character.right_imgs
				x_speed = 3
				y_speed = 0
			elif event.key == pygame.K_UP:
				dir = Character.up_imgs
				x_speed = 0
				y_speed = -3
			elif event.key == pygame.K_DOWN:
				dir = Character.down_imgs
				x_speed = 0
				y_speed = 3
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				if dir == Character.up_imgs:
					y_speed = 0
					x_speed = 0	
			if event.key == pygame.K_DOWN:
				if dir == Character.down_imgs:
					y_speed = 0
					x_speed = 0
			if event.key == pygame.K_LEFT:
				if dir == Character.left_imgs:
					y_speed = 0
					x_speed = 0
			if event.key == pygame.K_RIGHT:
				if dir == Character.right_imgs:
					y_speed = 0
					x_speed = 0
			img = Character.down_imgs[0]
			Character.img_idx = 0
	for y in range(13):
		for x in range(13):
			screen.window.blit(tile.tiles[0], (x * 48, y * 48))
	img = Character.animation(dir, 0.2)
	x_pos += x_speed
	y_pos += y_speed
	if x_pos < 0:
		x_pos = 0
	if y_pos < 0:
		y_pos = 0
	if x_pos > 624 - 48:
		x_pos = 624 - 48
	if y_pos > 624 - 48:
		y_pos = 624 - 58
	screen.window.blit(img, (x_pos, y_pos))
	pygame.display.update()
pygame.quit()