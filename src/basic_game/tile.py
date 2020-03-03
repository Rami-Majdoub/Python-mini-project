from player import Player
from enemy import Enemy
from block import Block
from potion import Potion
from door import Door

class Tile():
    empty_tile = '.'
    
    def __init__(self, row, column, actor=None):
        self.column = column
        self.row = row
        self.actor = actor

    def show(self):
        if self.actor == None: print(' {} '.format(Tile.empty_tile), end='')
        else: self.actor.show()
        
    def get_column(self): return self.column
    def get_row(self): return self.row
    
    def set_empty(self): self.actor = None
    def is_empty(self): return self.actor == None

    def set_actor(self, actor): self.actor = actor
    def get_actor(self): return self.actor

    # block, door, enemy, player, potion
    def contains_block(self): return isinstance(self.actor, Block)
    def contains_door(self): return isinstance(self.actor, Door)
    def contains_enemy(self): return isinstance(self.actor, Enemy)
    def contains_player(self): return isinstance(self.actor, Player)
    def contains_potion(self): return isinstance(self.actor, Potion)



    
