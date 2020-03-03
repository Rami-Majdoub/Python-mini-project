from random import randint

from map import Map
from player import Player
from door import Door
from enemy import Enemy
from block import Block
from potion import Potion

class LevelGenerator():
    def __init__(self, columns = 10, rows = 5, nb_blocks = 4, nb_enemies = 4, nb_potions = 2):
        # map
        self.my_map = Map(columns, rows)
        my_map = self.my_map
        # player, door
        self.player = Player(my_map= my_map, tile = my_map.get_empty_tile(), health = 3)
        self.door = Door(my_map)
        #enemy, block, potion
        self.enemies = []
        self.potions = []
        self.blocks = []
        for _ in range(nb_blocks): self.blocks.append( Block(my_map) )
        for _ in range(nb_enemies): self.enemies.append( Enemy(my_map, my_map.get_empty_tile(), 1) )
        for _ in range(nb_potions): self.potions.append( Potion(my_map, my_map.get_empty_tile(), randint(1, 3)) )

    def get_map(self): return self.my_map
    def get_player(self): return self.player
    def get_door(self): return self.door
    def get_blocks(self): return self.blocks
    def get_enemies(self): return self.enemies
    def get_potions(self): return self.potions
        
