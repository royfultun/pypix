import pygame
import os
#from tools import *

pygame.init()

#Window Settings
WIDTH, HEIGHT = [800, 600]
x, y = 160, 96
BOARD = pygame.Rect([x, y], [(WIDTH - x), (HEIGHT - y)])

BARS = []
x, y = x + 98, y
BARS.append(pygame.Rect([x, y], [(WIDTH - x), (HEIGHT - y)]))
x, y = x - 98, y + 98
BARS.append(pygame.Rect([x, y], [(WIDTH - x), (HEIGHT - y)]))

x, y = x + 98, y
GRID = pygame.Rect([x, y], [(WIDTH - x), (HEIGHT - y)])

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TRANSP = (250, 250, 250)

#Window Flags
WIN_HORIZONTAL = 1
WIN_VERTICAL = 2

#Baords
dir = os.path.join('data', 'boards')
for group in [os.path.join(dir, x) for x in os.listdir(dir) if '.py' in x]:
	group = open(group)
	exec group
	group.close()

#Images
#Image01
#Image02

try:
	import main
except(SystemExit): 
	pass