from actor import Actor

class Block(Actor):

    presentation = '#'

    def __init__(self, my_map, tile = None):
        super().__init__(my_map, tile, 0, False)

    def show(self):
        print(' {} '.format(Block.presentation), end='')
