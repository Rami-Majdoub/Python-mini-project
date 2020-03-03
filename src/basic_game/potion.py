from actor import Actor

class Potion(Actor):

    presentation = 'P'

    def __init__(self, my_map, tile, health):
        super().__init__(my_map, tile, health, False)

    def show(self):
        print(' {} '.format(Potion.presentation), end='')

    def __str__(self):
        return 'Potion ({}, {}) Health: {}'.format(super().get_tile().get_row(),super().get_tile().get_column() , super().get_health())
