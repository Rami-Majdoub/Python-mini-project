from actor import Actor
class Potion(Actor):
    presentation = 'P'
    def __init__(self, my_map, tile = None):
        super(Potion, self).__init__(my_map, tile, 5, False)

    def show(self):
        print(' {} '.format(Potion.presentation), end='')
