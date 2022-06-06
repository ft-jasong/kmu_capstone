import os.path
import pygame
from spritesheet import *

class Screen(object):
	margin = 40
	width = 600
	height = 520

	def __init__(self):
		self.screen_path = os.path.dirname(__file__) + '/../asset/screen/'
		self.window = None
		self.background = None
		self.main_logo = None

	def set_display(self):
		self.window = pygame.display.set_mode((self.width + self.margin , self.height + self.margin))
		self.background = pygame.image.load(self.screen_path + 'background.png')
		self.main_logo = Spritesheet(self.screen_path + 'mainlogo.png').image_at((0, 0, 996, 985), -1)
		self.main_logo = pygame.transform.scale(self.main_logo, (300, 300))
		pygame.display.set_caption("Copy Crazy Arcade")