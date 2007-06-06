import pygame
from pygame.locals import *
from const import *
from tools import *

cstyle = (lambda t, a, b: t and a or b)

class puzzlePoint(pygame.sprite.Sprite):
	def __init__(self, pos, size = 16, offset = [0, 0], state = False):
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
				(lambda i: ((i / 5) and i > 0) and 1 or 0)(point) #+ \
				#self.offset[i]
			)
		return add_points(p, self.offset)
		
class numBar(pygame.sprite.Sprite):
	def __init__(self, pos, nums = ['0', '1', '12', '3'], size = 16, offset = [0, 0], flags = 2):
		pygame.sprite.Sprite.__init__(self)
		self.nums = nums
		self.flags = flags
		self.size = size
		self.offset = offset
		self.text = pygame.font.SysFont('tahoma', size - 2)
		if self.flags & WIN_HORIZONTAL:
			dim = (100, size)
			self.nums.reverse()
		else:
			dim = (size, 100)
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
				((font_rect.right - dim[0]), font_rect.top - 1),
				dim
			)
			text = self.text.render(joined, True, BLACK)
			self.icon.blit(text, font_rect)

		else:
			for i in range(len(self.nums)):
				dim = self.text.size(self.nums[i])
				font_rect = self.icon.get_rect()
				font_rect = pygame.Rect(
					(font_rect.left, (font_rect.bottom - (self.text.get_linesize() * (i + 1)))),
					dim
				)
				text = self.text.render(self.nums[i], True, BLACK)
				self.icon.blit(text, font_rect)
				
	def set_rect(self, pos):
		if self.flags & WIN_HORIZONTAL:
			p = [
				BOARD.left,
				((self.size + 1) * pos[1]) + \
				(lambda i: ((i / 5) and i > 0) and 1 or 0)(pos[1]) + \
				BOARD.top
			]
		else:
			p = [
				((self.size + 1) * pos[0]) + \
				(lambda i: ((i / 5) and i > 0) and 1 or 0)(pos[0]) + \
				BOARD.left,
				BOARD.top
			]
		return add_points(p, self.offset)
				
				
		# for i in range(len(self.nums)):
			# dim = self.text.size(self.nums[i])
			# font_rect = self.icon.get_rect()
			# font_rect = pygame.Rect(
				# self.if_horizontal(
					# ((font_rect.right - ((self.size + len(self.nums[i])) * (i + 1))), font_rect.top - 1),
					# (font_rect.left, (font_rect.bottom - dim[1]))
				# ),
				# dim
			# )
			# text = self.text.render(self.nums[i], True, BLACK)
			
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