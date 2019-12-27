from tile import Tile
from random import randint

class Map():
    def __init__(self, columns=10, rows=5):
        self.nb_columns = columns
        self.nb_rows = rows
        # is there an other way ? reserver l'espace
        # self.tiles = [[Tile()] * self.nb_columns for i in range(self.nb_rows)]
        self.generate_new()

    def generate_new(self):
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
    
    def get_right_tile(self, tile): return self.tiles[tile.get_row()][tile.get_column()]
    def get_up_tile(self, tile): return self.tiles[tile.get_row()][tile.get_column()]
    def get_down_tile(self, tile): return self.tiles[tile.get_row()][tile.get_column()]

    def get_empty_tile(self):
        while True:
            c = randint(0, self.nb_columns - 1)
            r = randint(0, self.nb_rows - 1)
            tile = self.tiles[r][c]
            if (tile.is_empty()): return tile








        
