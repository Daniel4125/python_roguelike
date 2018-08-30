import pygame, sys
from pygame.locals import *
from constants import *
from components import *
from objects import *
from structs import *

clock = pygame.time.Clock()
global DISPLAYSURF




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
	for obj in game_objects:
		obj.draw(DISPLAYSURF)

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

	player_action = 'no action'

	while True:
		player_action = handle_keys()

		if player_action == 'QUIT':
			pygame.quit()
			sys.exit()
		
		elif player_action != 'no_action':
			for obj in game_objects:
				if obj.ai:
					obj.ai.take_turn(GAME_MAP)
		
		
		draw_game()
		clock.tick(60)
		

def initialize_game():
	'''This function initializes the main window, and pygame'''
	global DISPLAYSURF, GAME_MAP, player, game_objects
	pygame.init()
	pygame.display.set_caption('pygame')

	#set screen size
	DISPLAYSURF = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

	GAME_MAP = create_map()

	comp_creature = Creature('Greg')
	player = Actor(0, 0, 'python', S_PLAYER, comp_creature) # player is a creature

	comp_creature2 = Creature('Jackie')
	comp_ai = AI_Test()
	enemy = Actor(20, 10, 'crab', S_ENEMY, comp_creature2, comp_ai)


	game_objects = [player, enemy]



def handle_keys():
	# get player input
	events = pygame.event.get()

	for event in events:
		if event.type == QUIT:
			return 'QUIT'

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player.move(0, -1, GAME_MAP)
				return 'player_moved'
			if event.key == pygame.K_DOWN:
				player.move(0, 1, GAME_MAP)
				return 'player_moved'
			if event.key == pygame.K_LEFT:
				player.move(-1, 0, GAME_MAP)
				return 'player_moved'
			if event.key == pygame.K_RIGHT:
				player.move(1, 0, GAME_MAP)
				return 'player_moved'
	
	return 'no_action'






# ____                  _             __  __       _       _ _ _ 
#|  _ \ _   _ _ __   __| | ___ _ __  |  \/  | __ _(_)_ __ | | | |
#| | | | | | | '_ \ / _` |/ _ \ '__| | |\/| |/ _` | | '_ \| | | |
#| |_| | |_| | | | | (_| |  __/ |    | |  | | (_| | | | | |_|_|_|
#|____/ \__,_|_| |_|\__,_|\___|_|    |_|  |_|\__,_|_|_| |_(_|_|_)


if __name__ == '__main__':
	initialize_game()
	main_loop()


