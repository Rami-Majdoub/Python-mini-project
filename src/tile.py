from player import Player

class Tile():
    empty_tile = '0'
    
    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.content = Tile.empty_tile

    def set_content(self, actor):
        self.content = actor

    def get_column(self): return self.column
    def get_row(self): return self.row

    def show(self):
        print(' {} '.format(self.content), end='')

    def set_empty(self): self.content = Tile.empty_tile
    def is_empty(self): return self.content == Tile.empty_tile
