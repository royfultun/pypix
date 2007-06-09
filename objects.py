import pygame
from pygame.locals import *
from const import *
from tools import *

cstyle = (lambda t, a, b: t and a or b)

class puzzlePoint(pygame.sprite.Sprite):
	def __init__(self, pos, size = 16, state = False, offset = [0, 0]):
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
				((1 * (point / 5)) or 0)
			)
		return add_points(p, self.offset)
		
class numBar(pygame.sprite.Sprite):
	def __init__(self, pos, size = 16, nums = ['0', '1', '12', '3'], flags = 2, offset = [0, 0]):
		pygame.sprite.Sprite.__init__(self)
		self.nums = nums
		self.flags = flags
		self.size = size
		self.offset = offset
		self.text = pygame.font.SysFont('tahoma', 12)
		if self.flags & WIN_HORIZONTAL:
			dim = (96, size)
		else:
			dim = (size, 96)
			self.nums.reverse()
		self.icon = pygame.Surface(dim)
		self.rect = pygame.Rect(pos, dim)
		self.rect.topleft = self.set_rect(pos)
		
	def update(self):
		self.icon.fill(WHITE)
		if self.flags & WIN_HORIZONTAL:
			joined = '  '.join(self.nums)
			dim = self.text.size(joined)
			font_rect = self.icon.get_rect()
			font_rect = pygame.Rect(
				((font_rect.right - dim[0]) - 5, (font_rect.height / 2) - (self.text.get_height() / 2)),
				dim
			)
			text = self.text.render(joined, True, BLACK)
			self.icon.blit(text, font_rect)

		else:
			for i in range(len(self.nums)):
				dim = self.text.size(self.nums[i])
				font_rect = self.icon.get_rect()
				font_rect = pygame.Rect(
					((font_rect.width / 2) - (dim[0] / 2), (font_rect.bottom - (self.text.get_linesize() * (i + 1)))),
					dim
				)
				text = self.text.render(self.nums[i], True, BLACK)
				self.icon.blit(text, font_rect)
				
	def set_rect(self, pos):
		if self.flags & WIN_HORIZONTAL:
			p = [
				(BOARD.left + 1),
				((self.size + 1) * pos[1]) + \
				((1 * (pos[1] / 5)) or 0) + \
				(GRID.top + 1)
			]
		else:
			p = [
				((self.size + 1) * pos[0]) + \
				((1 * (pos[0] / 5)) or 0) + \
				(GRID.left + 1),
				(BOARD.top + 1)
			]
		return add_points(p, self.offset)
			
	def if_horizontal(self, horizontal, vertical):
		if self.flags & WIN_HORIZONTAL:
			return horizontal
		return vertical
		
		

		
# class puzzlePoint:
	# def __init__(self, position, state = False):
		# self.rect = set_rect(position)
		# self.x, self.y, self.width, self.height = self.rect
		# self.state = state
		
	# def toggle(self):
		# self.state = (lambda s: s and [False] or [True])(self.state)[0]
	
	# def get_state(self):
		# return self.state