from constants import *

#  ___  _     _           _       
# / _ \| |__ (_) ___  ___| |_ ___ 
#| | | | '_ \| |/ _ \/ __| __/ __|
#| |_| | |_) | |  __/ (__| |_\__ \
# \___/|_.__// |\___|\___|\__|___/
#          |__/                   

class Actor:
	'''Interactable object in the game'''
	def __init__(self, x, y, name, sprite, creature=None, ai=None):
         self.x = x #map address, not pixel address
         self.y = y
         self.sprite = sprite

        #components
         self.creature = creature # player.creature would reference the creature component
         if creature:
            creature.owner = self # the creature blongs the Actor that called it
         
         self.ai = ai
         if ai:
            ai.owner = self


	def draw(self, DISPLAYSURF):
         '''Draw actor on the main surface'''
         DISPLAYSURF.blit(self.sprite, (self.x*CELL_WIDTH, self.y*CELL_HEIGHT))

	def move(self, dx, dy, game_map):
        #check if path is blocked before moving
         if game_map[self.x + dx][self.y + dy].block_path == False:
            self.x += dx
            self.y += dy
