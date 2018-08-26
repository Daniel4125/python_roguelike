import pygame, sys
from pygame.locals import *
from constants import *

clock = pygame.time.Clock()

def initialize():
	'''This function initializes the main window, and pygame'''
	global DISPLAYSURF
	pygame.init()
	pygame.display.set_caption('pygame')

	#set screen size
	DISPLAYSURF = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

def update():
	'''The main game loop'''
	while True:
		# get player input
		events = pygame.event.get()

		for event in events:
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		draw_game()
		clock.tick(60)


def draw_game():
	global DISPLAYSURF

	#clear the surface
	DISPLAYSURF.fill(BLUE)

	#TODO draw the map

	#draw the character

	#update the display
	pygame.display.flip()


if __name__ == '__main__':
	initialize()
	update()


