import pygame
from pygame.locals import *
from const import *

cstyle = (lambda t, a, b: t and a or b)

class puzzlePoint(pygame.sprite.Sprite):
	def __init__(self, pos, size = 16, offset = (0, 0), state = False):
		pygame.sprite.Sprite.__init__(self)
		self.size = size
		self.offset = offset
		self.state = state
		self.color = cstyle(self.state, BLACK, WHITE)
		self.icon = pygame.Surface((size, size))
		self.rect = self.icon.get_rect()
		self.rect.topleft = self.set_rect(pos)
		
	def update(self):
		self.icon.fill(self.color)

	def toggle(self):
		self.state = (lambda s: s and [False] or [True])(self.state)[0]
		self.color = cstyle(self.state, BLACK, WHITE)
	
	def get_state(self):
		return self.state
		
	def set_rect(self, pos):
		p = []
		for i in range(2):
			point = pos[i]
			p.append(
				((self.size + 1) * point) + \
				(lambda i: ((i / 5) and i > 0) and 1 or 0)(point) + \
				self.offset[i]
			)
		return p
		
# class numBar(pygame.sprite.Sprite):
	# def __init__(self, pos, list = ['0'], size = 16, offset = (0, 0), flags = 1):
		# pygame.sprite.Sprite.__init__(self)
		# self.list = list
		# self.flags = flags
		# self.font = pygame.font.SysFont('tahoma', size - 2)
		# dem = (lambda f: f & WIN_HORIZONTAL and (50, size) or (size, 50))(flags)
		# self.icon = pygame.Surface(dem)
		# self.rect = (pos, dem)
		
	# def update:
		# font_rect = pygame.Rect(
			# self.rect.topleft, 
			# (lambda f: f & WIN_HORIZONTAL and (, self.rect.height) or (size, 50))(flags)
		# )
		# for n in self.list:
			
			# self.icon.blit
		

		
# class puzzlePoint:
	# def __init__(self, position, state = False):
		# self.rect = set_rect(position)
		# self.x, self.y, self.width, self.height = self.rect
		# self.state = state
		
	# def toggle(self):
		# self.state = (lambda s: s and [False] or [True])(self.state)[0]
	
	# def get_state(self):
		# return self.state