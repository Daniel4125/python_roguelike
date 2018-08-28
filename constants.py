import pygame

#GAME SIZES
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

#MAP
MAP_WIDTH = 30
MAP_HEIGHT = 30
CELL_WIDTH = 32
CELL_HEIGHT = 32

COLOUR_BLACK = ( 0, 0, 0)
COLOUR_WHITE = (255, 255, 255)
COLOUR_RED = (255, 0, 0)
COLOUR_GREEN = (0, 255, 0)
COLOUR_BLUE = (0, 0, 255)

#SPRITES
S_PLAYER = pygame.image.load('sprites/player.png')
S_WALL = pygame.image.load('sprites/wall1.png')
S_FLOOR = pygame.image.load('sprites/floor.png')
S_ENEMY = pygame.image.load('sprites/crab.png')
