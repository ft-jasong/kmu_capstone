import pygame
from pyparsing import col
import spritesheet as ss
import os.path

class Map(object):
	def __init__(self):
		self.pirate = Pirate()

class Pirate(object):
	def __init__(self):
		self.cur_path = os.path.dirname(__file__)
		self.map_path = self.cur_path + '/../asset/map/'
		self.block_ss = ss.Spritesheet(self.map_path + 'map_pirate_object1.png')
		self.tile_ss = ss.Spritesheet(self.map_path + 'map_pirate_tile2.png')
		self.tiles = self.tile_ss.load_strip((0, 0, 40, 40), 15, colorkey=None)
		self.blocks = []
		self.block_up = self.block_ss.image_at((1, 1, 42, 7), colorkey=-1)
		self.block_down = self.block_ss.image_at((1, 9, 40, 40), colorkey=-1)
		self.tile_board = [
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			[3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3],
			[3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3],
			[3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3],
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			[3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3],
			[3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3],
			[3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3],
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
		]
		self.block_board = [
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1],
			[-1, 0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1],
			[-1, 0, 1, -1, -1, 2, -1, -1, -1, 2, -1, -1, 1, 0, -1],
			[-1, 0, 1, -1, -1, 2, -1, -1, -1, 2, -1, -1, 1, 0, -1],
			[-1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, 0, 0, 2, 2, 0, -1, -1, -1, 0, 2, 2, 0, 0, -1],
			[-1, 0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1],
			[-1, 0, 1, -1, -1, 0, -1, -1, -1, 0, -1, -1, 1, 0, -1],
			[-1, 0, 1, -1, -1, 0, -1, -1, -1, 0, -1, -1, 1, 0, -1],
			[-1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
		]
		self.init_blocks()


	def init_blocks(self):
		block_steel_sprite = ss.Spritesheet(self.map_path + 'map_pirate_block_steel.png')
		block_normal_sprite = ss.Spritesheet(self.map_path + 'map_pirate_object1.png')
		block_box_sprite = ss.Spritesheet(self.map_path + 'map_pirate_block_box.png')
		block_steel = []
		block_normal = []
		block_box = []
		block_steel.append(block_steel_sprite.image_at((0, 0, 40, 7), colorkey=-1))
		block_steel.append(block_steel_sprite.image_at((0, 7, 40, 40), colorkey=-1))
		block_normal.append(block_normal_sprite.image_at((1, 1, 40, 7), colorkey=-1))
		block_normal.append(block_normal_sprite.image_at((1, 9, 40, 40), colorkey=-1))
		block_box.append(block_box_sprite.image_at((0, 0, 40, 7), colorkey=-1))
		block_box.append(block_box_sprite.image_at((0, 8, 40, 40), colorkey=-1))
		self.blocks.append(block_steel)
		self.blocks.append(block_normal)
		self.blocks.append(block_box)