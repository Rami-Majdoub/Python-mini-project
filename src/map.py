from tile import Tile
from player import Player
from random import randint

class Map():
    def __init__(self, columns=10, rows=5):
        self.nb_columns = columns
        self.nb_rows = rows
        self.generate_new_empty()

    def generate_new(self): self.generate_new_empty()
    def generate_new_empty(self):
        self.tiles= []
        for i in range(self.nb_rows):
            row = []
            for j in range(self.nb_columns):
                row.append(Tile(i, j))
            self.tiles.append(row)

    def show(self):
        for i in range(self.nb_rows):
            for j in range(self.nb_columns):
                self.tiles[i][j].show()
            print()

    def get_left_tile(self, tile):
        if(tile.get_column() > 0):
            return self.tiles[tile.get_row()][tile.get_column() - 1] # bug here
        else: return None
        
    def get_right_tile(self, tile):
        if(tile.get_column() < self.nb_columns - 1):
            return self.tiles[tile.get_row()][tile.get_column() + 1] # bug here
        else: return None

    def get_up_tile(self, tile):
        if(tile.get_row() > 0):
            return self.tiles[tile.get_row() - 1][tile.get_column()] # bug here
        else: return None
        
    def get_down_tile(self, tile):
        if(tile.get_row() < self.nb_rows - 1):
            return self.tiles[tile.get_row() + 1][tile.get_column()] # bug here
        else: return None
        
    def get_empty_tile(self):
        while True:
            c = randint(0, self.nb_columns - 1)
            r = randint(0, self.nb_rows - 1)
            tile = self.tiles[r][c]
            if (tile.is_empty()): return tile

    






        
