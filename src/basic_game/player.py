from movingActor import MovingActor

class Player(MovingActor):
    
    presentation = 'X'

    def __init__(self, my_map, tile = None, health = 1):
        super().__init__(my_map, tile, health, False)

    def show(self):
        print(' {} '.format(Player.presentation), end='')

    def __str__(self):
        return 'player Health: {}'.format(super().get_health())
