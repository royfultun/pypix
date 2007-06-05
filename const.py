import pygame

pygame.init()

#Window Settings
WIDTH, HEIGHT = [800, 600]
x, y = [200, 100]
BOARD = pygame.Rect([x, y], [(HEIGHT - y), (WIDTH - x)])

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TRANSP = (250, 250, 250)

#Window Flags
WIN_HORIZONTAL = 1
WIN_VERTICAL = 2

#Images
#Image01
#Image02

try:
	import main
except(SystemExit): 
	pass
