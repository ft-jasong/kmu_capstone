from spritesheet import Spritesheet
import os.path

class Map(object):
	def __init__(self):
		self.pirate = Pirate()

class Pirate(object):
	def __init__(self):
		self.cur_path = os.path.dirname(__file__)
		self.map_path = self.cur_path + '/../asset/map/'
		self.tile_ss = Spritesheet(self.map_path + 'map_pirate_tile2.png')
		self.tiles = self.tile_ss.load_strip((0, 0, 40, 40), 15, colorkey=None)
		self.blocks = []
		self.stage1_tile = [
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			[3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3],
			[3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3],
			[3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3],
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			[3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3],
			[3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3],
			[3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3],
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
		]
		self.stage1_block = [
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1],
			[-1, 0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1],
			[-1, 0, 1, -1, -1, 2, -1, -1, -1, 2, -1, -1, 1, 0, -1],
			[-1, 0, 1, -1, -1, 2, -1, -1, -1, 2, -1, -1, 1, 0, -1],
			[-1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, 0, 0, 2, 2, 0, -1, -1, -1, 0, 2, 2, 0, 0, -1],
			[-1, 0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1],
			[-1, 0, 1, -1, -1, 0, -1, -1, -1, 0, -1, -1, 1, 0, -1],
			[-1, 0, 1, -1, -1, 0, -1, -1, -1, 0, -1, -1, 1, 0, -1],
			[-1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
		]
		self.stage2_tile = []
		self.stage2_block = []
		self.boss_tile = [
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
			[3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
		]
		self.boss_block = [
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
		]
		self.init_blocks()


	def init_blocks(self):
		block_steel_sprite = Spritesheet(self.map_path + 'map_pirate_block_steel.png')
		block_normal_sprite = Spritesheet(self.map_path + 'map_pirate_object1.png')
		block_box_sprite = Spritesheet(self.map_path + 'map_pirate_block_box.png')
		block_stage2_sprite = Spritesheet(self.map_path + 'map_pirate_tile6.png')
		block_steel = []
		block_normal = []
		block_box = []
		block_pole = []
		block_blue = []
		block_green = []
		block_orange = []
		block_red = []
		block_steel.append(block_steel_sprite.image_at((0, 0, 40, 7), colorkey=-1))
		block_steel.append(block_steel_sprite.image_at((0, 7, 40, 40), colorkey=-1))
		block_steel.append(int(7))
		block_normal.append(block_normal_sprite.image_at((1, 1, 40, 7), colorkey=-1))
		block_normal.append(block_normal_sprite.image_at((1, 9, 40, 40), colorkey=-1))
		block_normal.append(int(7))
		block_box.append(block_box_sprite.image_at((0, 0, 40, 7), colorkey=-1))
		block_box.append(block_box_sprite.image_at((0, 8, 40, 40), colorkey=None))
		block_box.append(int(7))
		block_pole.append(block_box_sprite.image_at((0, 0, 40, 7), colorkey=-1))
		block_pole.append()
		block_pole.append(26)
		block_blue.append()
		block_blue.append()
		block_blue.append(19)
		block_green.append()
		block_green.append()
		block_green.append(19)
		block_orange.append()
		block_orange.append()
		block_orange.append(19)
		block_red.append()
		block_red.append()
		block_red.append(19)
		self.blocks.append(block_steel)
		self.blocks.append(block_normal)
		self.blocks.append(block_box)
		self.blocks.append(block_pole)
		self.blocks.append(block_blue)
		self.blocks.append(block_green)
		self.blocks.append(block_orange)
		self.blocks.append(block_red)

# Block 클래스 하나 사용해도 괜찮을것 같음. 이 밑은 테스트용 클래스. Map 내부에서 list로 사용하는 것과 비교해서 사용 예정.

# class Block(object):
# 	def __init__(self):
# 		self.img = None
# 		self.breakable = 0

# class SteelBlock(Block):
