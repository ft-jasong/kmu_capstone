from spritesheet import Spritesheet
import os.path

class Pirate(object):
	stage1_tile = [
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
	stage1_block = [
		[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
		[-1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1],
		[-1, 0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1],
		[-1, 0, 1, -1, -1, 2, -1, -1, -1, 2, -1, -1, 1, 0, -1],
		[-1, 0, 1, -1, -1, 2, -1, -1, -1, 2, -1, -1, 1, 0, -1],
		[-1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1],
		[-1, -1, -1, -1, -1, -1, -1, 8, -1, -1, -1, -1, -1, -1, -1],
		[-1, 0, 0, 2, 2, 0, -1, -1, -1, 0, 2, 2, 0, 0, -1],
		[-1, 0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1],
		[-1, 0, 1, -1, -1, 0, -1, -1, -1, 0, -1, -1, 1, 0, -1],
		[-1, 0, 1, -1, -1, 0, -1, -1, -1, 0, -1, -1, 1, 0, -1],
		[-1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1],
		[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
		]
	stage2_tile = [
		[3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
		[2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2],
		[3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
		[2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2],
		[3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
		[2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2],
		[3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
		[2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2],
		[3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
		[2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2],
		[3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
		[2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2],
		[3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
		]
	stage2_block = [
		[-1, -1, +1, -1, +1, -1, -1, -1, -1, -1, +1, -1, +1, -1, -1],
		[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
		[-1, -1, +3, -1, +2, -1, -1, -1, -1, -1, +2, -1, +3, -1, -1],
		[-1, -1, +4, -1, +2, -1, -1, -1, -1, -1, +2, -1, +4, -1, -1],
		[-1, -1, +5, +1, +2, +2, +2, +2, +2, +2, +2, +1, +5, -1, -1],
		[-1, -1, +6, -1, -1, -1, -1, -1, -1, -1, -1, -1, +6, -1, -1],
		[-1, -1, +7, +1, +8, +8, +8, +8, +8, +8, +8, +1, +7, -1, -1],
		[-1, -1, +5, -1, -1, -1, -1, -1, -1, -1, -1, -1, +5, -1, -1],
		[-1, -1, +4, +1, -1, -1, -1, -1, -1, -1, -1, +1, +4, -1, -1],
		[-1, -1, +3, -1, -1, -1, -1, -1, -1, -1, -1, -1, +3, -1, -1],
		[-1, -1, -1, +1, -1, -1, -1, -1, -1, -1, -1, +1, -1, -1, -1],
		[-1, -1, -1, -1, +1, -1, -1, -1, -1, -1, +1, -1, -1, -1, -1],
		[-1, -1, -1, -1, -1, +1, +3, +4, +3, +1, -1, -1, -1, -1, -1],
		]
	boss_tile = [
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
	boss_block = [
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
	def __init__(self):
		self.cur_path = os.path.dirname(__file__)
		self.map_path = self.cur_path + '/../asset/map/'
		self.tile_ss = Spritesheet(self.map_path + 'map_pirate_tile2.png')
		self.tiles = self.tile_ss.load_strip((0, 0, 40, 40), 15, colorkey=None)
		self.blocks = []
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
		block_turtle = []
		block_steel.append(block_steel_sprite.image_at((0, 0, 40, 7), colorkey=-1))
		block_steel.append(block_steel_sprite.image_at((0, 7, 40, 40), colorkey=None))
		block_steel.append(int(7))
		block_normal.append(block_normal_sprite.image_at((1, 1, 40, 7), colorkey=-1))
		block_normal.append(block_normal_sprite.image_at((1, 9, 40, 40), colorkey=None))
		block_normal.append(int(7))
		block_box.append(block_box_sprite.image_at((0, 0, 40, 7), colorkey=-1))
		block_box.append(block_box_sprite.image_at((0, 8, 40, 40), colorkey=None))
		block_box.append(int(7))
		block_pole.append(block_stage2_sprite.image_at((280, 94, 40, 26), colorkey=-1))
		block_pole.append(block_stage2_sprite.image_at((280, 120, 40, 40), colorkey=None))
		block_pole.append(26)
		block_blue.append(block_stage2_sprite.image_at((440, 100, 40, 18), colorkey=-1))
		block_blue.append(block_stage2_sprite.image_at((440, 118, 40, 40), colorkey=None))
		block_blue.append(18)
		block_green.append(block_stage2_sprite.image_at((480, 100, 40, 18), colorkey=-1))
		block_green.append(block_stage2_sprite.image_at((480, 118, 40, 40), colorkey=None))
		block_green.append(18)
		block_orange.append(block_stage2_sprite.image_at((520, 100, 40, 18), colorkey=-1))
		block_orange.append(block_stage2_sprite.image_at((520, 118, 40, 40), colorkey=None))
		block_orange.append(18)
		block_red.append(block_stage2_sprite.image_at((560, 100, 40, 18), colorkey=-1))
		block_red.append(block_stage2_sprite.image_at((560, 118, 40, 40), colorkey=None))
		block_red.append(18)
		block_turtle.append(block_stage2_sprite.image_at((521, 22, 40, 16), colorkey=-1))
		block_turtle.append(block_stage2_sprite.image_at((521, 38, 40, 40), colorkey=None))
		block_turtle.append(16)
		self.blocks.append(block_steel) # NUM 0
		self.blocks.append(block_normal) # NUM 1
		self.blocks.append(block_box) # NUM 2
		self.blocks.append(block_pole) # NUM 3
		self.blocks.append(block_blue) # NUM 4
		self.blocks.append(block_green) # NUM 5
		self.blocks.append(block_orange) # NUM 6
		self.blocks.append(block_red) # NUM 7
		self.blocks.append(block_turtle) # NUM 8


class Map(object):
	stages = [
		[Pirate.stage1_tile, Pirate.stage1_block],
		[Pirate.stage2_tile, Pirate.stage2_block],
		[Pirate.boss_tile, Pirate.boss_block]
		]
	def __init__(self):
		self.pirate = Pirate()


# Block 클래스 하나 사용해도 괜찮을것 같음. 이 밑은 테스트용 클래스. Map 내부에서 list로 사용하는 것과 비교해서 사용 예정.

# class Block(object):
# 	def __init__(self):
# 		self.img = None
# 		self.breakable = 0

# class SteelBlock(Block):
