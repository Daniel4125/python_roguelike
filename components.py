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

class AI_Test:
    '''Once per turn execute'''

    def take_turn(self, game_map):
        self.owner.move(-1, 0, game_map)