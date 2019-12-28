from player import Player

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
