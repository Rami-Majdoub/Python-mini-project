from movingActor import movingActor
from random import randint

class Enemy(movingActor):
    presentation = '*'
    def __init__(self, my_map, tile, health):
        super(Enemy, self).__init__(my_map, tile, health, True)

    def show(self):
        print(' {} '.format(Enemy.presentation), end='')

    def move(self):
        moves = super().get_possible_moves()
        super().move( moves[randint(0, len(moves) -1)] )
