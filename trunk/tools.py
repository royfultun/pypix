import pygame
from pygame.locals import *

def create_screen(size = (640, 480)):
	return pygame.display.set_mode(size)
	
def load_image(img):
	return pygame.image.load(img).convert()