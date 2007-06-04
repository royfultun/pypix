import pygame
import os, sys

from pygame.locals import *
from const import *
from tools import *
from objects import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class PyPixMain():

	def __init__(self, width = 640, height = 480):

		pygame.init()
		
		self.width = width
		self.height = height
		self.screen = create_screen((self.width, self.height))
		self.object_layer = pygame.Rect(
			(128,64),
			((self.width - 128), (self.height - 64))
		)

		self.objects = []

		for i in range(10):
			for j in range(10):
				self.objects.append(puzzlePoint([i, j], offset = (128, 64)))
	
	def mainLoop(self):
		while 1:
			mouse_pos = 0
			for event in pygame.event.get():
				if event.type == QUIT:
					return
					
				if event.type == MOUSEBUTTONDOWN and event.button == 1:
					mouse_pos = event.pos
					
			self.screen.fill(WHITE)
			self.screen.fill(BLACK, self.object_layer)
			
			for object in self.objects:
				if mouse_pos and object.rect.collidepoint(mouse_pos):
					object.toggle()
				object.update()
				self.screen.blit(object.icon, object.rect)
				
			pygame.display.update()
		
if __name__ == "__main__":
	game = PyPixMain()
	game.mainLoop()
	