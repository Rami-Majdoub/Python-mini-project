from movingActor import movingActor
class Player(movingActor):
    presentation = 'X'
    def __init__(self, my_map, tile = None, health = 1):
        super(Player, self).__init__(my_map, tile, health, False)

    def show(self):
        print(' {} '.format(Player.presentation), end='')
