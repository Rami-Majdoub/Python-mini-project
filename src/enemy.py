from movingActor import movingActor
class Enemy(movingActor):
    def __init__(self, my_map, tile, health):
        super(Player, self).__init__(my_map, tile, health, True)
