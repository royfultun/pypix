import pygame
import os
from pygame.locals import *

def create_screen(size = (640, 480)):
	return pygame.display.set_mode(size)
	
def load_image(img):
	return pygame.image.load(os.path.join("data", "images", img)).convert()
	
def load_sound(snd):
	return pygame.mixer.sound(os.path.join("data", "sounds", snd))
	
def add_points(seta, setb):
	"Add two sets of points together"
	return map((lambda a, b: a + b), seta, setb)
	
def sub_points(seta, setb):
	"Subtract two sets of points"
	return map((lambda a, b: a - b), seta, setb)