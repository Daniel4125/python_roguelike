import pygame, sys
from pygame.locals import *
from constants import *

clock = pygame.time.Clock()


#____  _                   _       
#/ ___|| |_ _ __ _   _  ___| |_ ___ 
#\___ \| __| '__| | | |/ __| __/ __|
# ___) | |_| |  | |_| | (__| |_\__ \
#|____/ \__|_|   \__,_|\___|\__|___/
                                   
class struct_Tile:
	def __init__(self, block_path):
		 self.block_path = block_path


#  ___  _     _           _       
# / _ \| |__ (_) ___  ___| |_ ___ 
#| | | | '_ \| |/ _ \/ __| __/ __|
#| |_| | |_) | |  __/ (__| |_\__ \
# \___/|_.__// |\___|\___|\__|___/
#          |__/                   

class Actor:
	'''Interactable object in the game'''
	def __init__(self, x, y, name, sprite, creature=None):
		 self.x = x #map address, not pixel address
		 self.y = y
		 self.sprite = sprite

		 if creature:
			 self.creature = creature # player.creature would reference the creature component
			 creature.owner = self # the creature blongs the Actor that called it


	def draw(self):
		DISPLAYSURF.blit(self.sprite, (self.x*CELL_WIDTH, self.y*CELL_HEIGHT))

	def move(self, dx, dy):
		#check if path is blocked before moving
		if GAME_MAP[self.x + dx][self.y + dy].block_path == False:
			self.x += dx
			self.y += dy


# ____                                             _       
#/ ___|___  _ __ ___  _ __   ___  _ __   ___ _ __ | |_ ___ 
#| |   / _ \| '_ ` _ \| '_ \ / _ \| '_ \ / _ \ '_ \| __/ __|
#| |__| (_) | | | | | | |_) | (_) | | | |  __/ | | | |_\__ \
#\____\___/|_| |_| |_| .__/ \___/|_| |_|\___|_| |_|\__|___/
#                     |_|          

class Creature:
	'''Creatures have health, can damage
	other objects by attacking them. Can also die'''
	
	def __init__(self, name_instance, hp = 10):
		self.name_instance = name_instance
		self.hp = hp		

#class Item:

#class Container:



# __  __             
#|  \/  | __ _ _ __  
#| |\/| |/ _` | '_ \ 
#| |  | | (_| | |_) |
#|_|  |_|\__,_| .__/ 
#             |_|    

def create_map():
	new_map = [[struct_Tile(False) for y in range(0, MAP_HEIGHT)] for x in range(0, MAP_WIDTH)]

	new_map[10][10].block_path = True
	new_map[10][15].block_path = True

	return new_map


# ____                     _             
#|  _ \ _ __ __ ___      _(_)_ __   __ _ 
#| | | | '__/ _` \ \ /\ / / | '_ \ / _` |
#| |_| | | | (_| |\ V  V /| | | | | (_| |
#|____/|_|  \__,_| \_/\_/ |_|_| |_|\__, |
#                                  |___/

def draw_game():
	global DISPLAYSURF

	#clear the surface
	DISPLAYSURF.fill(COLOUR_BLUE)

	#draw the map
	draw_map(GAME_MAP)

	#draw the characters
	enemy.draw()
	player.draw()

	#update the display
	pygame.display.flip()

def draw_map(map_to_draw):
	for x in range(0,MAP_WIDTH):
		for y in range(0,MAP_HEIGHT):
			if map_to_draw[x][y].block_path == True:
				#draw wall
				DISPLAYSURF.blit((S_WALL), (x*CELL_WIDTH, y*CELL_HEIGHT))
			else:
				#draw floor
				DISPLAYSURF.blit((S_FLOOR), (x*CELL_WIDTH, y*CELL_HEIGHT))


#  ____                      
# / ___| __ _ _ __ ___   ___ 
#| |  _ / _` | '_ ` _ \ / _ \
#| |_| | (_| | | | | | |  __/
# \____|\__,_|_| |_| |_|\___|

def main_loop():
	'''The main game loop'''
	while True:
		# get player input
		events = pygame.event.get()

		for event in events:
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					player.move(0, -1)
				if event.key == pygame.K_DOWN:
					player.move(0, 1)
				if event.key == pygame.K_LEFT:
					player.move(-1, 0)
				if event.key == pygame.K_RIGHT:
					player.move(1, 0)

		draw_game()
		clock.tick(60)
		

def initialize_game():
	'''This function initializes the main window, and pygame'''
	global DISPLAYSURF, GAME_MAP, player, enemy
	pygame.init()
	pygame.display.set_caption('pygame')

	#set screen size
	DISPLAYSURF = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

	GAME_MAP = create_map()

	comp_creature = Creature('Greg')
	player = Actor(0, 0, 'python', S_PLAYER, comp_creature) # player is a creature

	comp_creature2 = Creature('Jackie')
	enemy = Actor(15, 10, 'crab', S_ENEMY, comp_creature2)



# ____                  _             __  __       _       _ _ _ 
#|  _ \ _   _ _ __   __| | ___ _ __  |  \/  | __ _(_)_ __ | | | |
#| | | | | | | '_ \ / _` |/ _ \ '__| | |\/| |/ _` | | '_ \| | | |
#| |_| | |_| | | | | (_| |  __/ |    | |  | | (_| | | | | |_|_|_|
#|____/ \__,_|_| |_|\__,_|\___|_|    |_|  |_|\__,_|_|_| |_(_|_|_)


if __name__ == '__main__':
	initialize_game()
	main_loop()


