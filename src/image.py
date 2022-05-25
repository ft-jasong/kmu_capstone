import pygame

def image_colorkey(img, rectangle, colorkey = None):
	"Loads image from x, y, x+offset, y+offset"
	rect = pygame.Rect(rectangle)
	image = pygame.Surface(rect.size).convert()
	image.blit(img, (0, 0), rect)
	if colorkey != None:
		if colorkey == -1:
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, pygame.RLEACCEL)
	return image

def image_info(img, width, height):
	ret_li = []
	ret_li.append(img)
	ret_li.append(width)
	ret_li.append(height)
	return ret_li
