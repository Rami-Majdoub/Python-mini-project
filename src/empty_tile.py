from player import Player

class EmptyTile(Tile):
    representation = '0'
    
    def __init__(self, column, row):
        super(EmptyTile).__init__(column, row)

    def show(self):
        print(' {} '.format(EmptyTile.representation), end='')

    def is_empty(self): return True
