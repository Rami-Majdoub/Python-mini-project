class Actor():
    def __init__(self, my_map, tile = None, health=1, is_enemy=False):
        self.my_map = my_map

        if(tile == None): self.my_tile = my_map.get_empty_tile()
        else: self.my_tile = tile
        self.my_tile.set_actor(self)
        
        self.helth = health
        self.is_enemy = is_enemy
        self.dead = False

    def show(self):pass
    def get_tile(self): return self.my_tile
    def set_tile(self, new_tile): self.my_tile = new_tile
    
    def get_health(self): return self.health
    def is_enemy(self): return self.is_enemy

    def is_dead(self):return self.dead
    def die(self): self.dead = True
