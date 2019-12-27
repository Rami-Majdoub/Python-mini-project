from movingActor import movingActor
class Player(movingActor):
    def __init__(self, my_map, tile, health):
        super(Player, self).__init__(my_map, tile, health, False)
