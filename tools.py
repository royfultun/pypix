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

def get_grouplist(board):
	"""Returns two arrays with an array for each direction.
	Example:
	[
	[1, 0, 0, 1, 1], 
	[0, 0, 1, 1, 0], 
	[1, 1, 1, 1, 1], 
	[0, 0, 0, 0, 0], 
	[1, 1, 0, 1, 1]
	]
	X List: [[1, 2], [2], [5], [0], [2, 2]]
	Y List: [[1, 1, 1], [1, 1], [2], [3, 1], [1, 1, 1]]"""
	x_len = len(board)
	y_len = len(board[0])
	
	x_list = [[0] for i in range(x_len)]
	y_list = [[0] for i in range(y_len)]
	
	for row in range(x_len):
		for column in range(y_len):
			x_list[row][-1] += board[row][column]
			y_list[column][-1] += board[row][column]
			
			if column < (y_len - 1) and x_list[row][-1] and not board[row][column + 1]:
				x_list[row].append(0)
			if row < (x_len - 1) and y_list[column][-1] and not board[row + 1][column]:
				y_list[column].append(0)
			

			if row == (x_len - 1) and len(y_list[column]) > 1 and not y_list[column][-1]:
				del y_list[column][-1]
		if len(x_list[row]) > 1 and not x_list[row][-1]:
			del x_list[row][-1]
		
	#Convert the arrays to strings so pygame.font can parse them.
	return [[[str(i) for i in l] for l in x_list], [[str(i) for i in l] for l in y_list]]
	