from actor import Actor
class Block(Actor):
    def __init__(self, my_map, tile, health):
        super(Block, self).__init__(my_map, tile, 0, False)
