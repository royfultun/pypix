import pygame
import os, sys

from pygame.locals import *
#from const import *
from tools import *
from objects import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class PyPixMain():

	def __init__(self, width = 800, height = 600):
		
		self.width = width
		self.height = height
		self.screen = create_screen((self.width, self.height))

		self.objects = []
		self.numbars = []
		
		for i in range(10):
			self.numbars.append(numBar(
				[0, i], 
				flags = WIN_HORIZONTAL,
				offset = [1,103]
			))
			self.numbars.append(numBar(
				[i, 0], 
				flags = WIN_VERTICAL,
				offset = [103,1]
			))
			for j in range(10):
				self.objects.append(
					puzzlePoint(
						[i, j], 
						offset = add_points(BOARD.topleft, [103,103])
					)
				)
	
	def mainLoop(self):
		while 1:
			mouse_pos = 0
			for event in pygame.event.get():
				if event.type == QUIT:
					return
					
				if event.type == MOUSEBUTTONDOWN and event.button == 1:
					mouse_pos = event.pos
					
			self.screen.fill(WHITE)
			self.screen.fill(BLACK, BOARD)
			
			for bar in self.numbars:
				bar.update()
				self.screen.blit(bar.icon, bar.rect)
			
			for object in self.objects:
				if mouse_pos and object.rect.collidepoint(mouse_pos):
					object.toggle()
				object.update()
				self.screen.blit(object.icon, object.rect)
				
			pygame.display.update()
		
#if __name__ == "__main__":
game = PyPixMain(WIDTH, HEIGHT)
game.mainLoop()
	