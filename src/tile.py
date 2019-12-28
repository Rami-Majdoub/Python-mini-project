from player import Player

class Tile():
    empty_tile = '0'
    
    def __init__(self, row, column, actor=None):
        self.column = column
        self.row = row
        self.actor = actor
    
    def get_column(self): return self.column
    def get_row(self): return self.row

    def show(self):
        if self.actor == None:
            print(' {} '.format(Tile.empty_tile), end='')
        else: self.actor.show()
    # def show(self): print(' {} '.format(self.content), end='')

    def set_empty(self): self.actor = None
    def is_empty(self): return self.actor == None
    def set_actor(self, actor): self.actor = actor
