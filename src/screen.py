import pygame

class Screen(object):
	margin = 40
	width = 600
	height = 520

	def set_display(self):
		self.window = pygame.display.set_mode((self.width + self.margin , self.height + self.margin))
		pygame.display.set_caption("Copy Crazy Arcade")