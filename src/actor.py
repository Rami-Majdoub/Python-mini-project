class Actor():
    def __init__(self, my_map, tile, health, is_enemy):
        self.my_map = my_map
        self.my_tile = tile
        self.helth = health
        self.is_enemy = is_enemy

    def get_tile(self): return self.my_tile
    def set_tile(self, new_tile): self.my_tile = new_tile
    
    def get_health(self): return self.health
    def is_enemy(self): return self.is_enemy
