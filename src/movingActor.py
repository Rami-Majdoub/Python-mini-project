from actor import Actor
class movingActor(Actor):
    def __init__(self, my_map, tile, health, is_enemy):
        super(movingActor, self).__init__(my_map, tile, health, is_enemy)

    def can_go_left(self):
        if (self.my_map.get_left_tile(self.my_tile) == None): # bug here
            return False # there is no tile on my left
        else: return True # check for block tiles and other
            #return it doesn't has a block & different types (enemy !enemy)
        
    def can_go_right(self): return True
    def can_go_up(self): return True
    def can_go_down(self): return True

    """
    " return a table contains the possible entrees for the moves
    """
    def get_possible_moves(self):
        moves = []
        if self.can_go_left(): moves.append('l')
        if self.can_go_right(): moves.append('r')
        if self.can_go_up(): moves.append('u')
        if self.can_go_down(): moves.append('d')
        return moves

    def move(self, direction):
        if (direction == 'l'):
            new_tile = self.my_map.get_left_tile(self.my_tile)
            super().set_tile(new_tile)
        elif (direction == 'r'):
            new_tile = self.my_map.get_right_tile(self.my_tile)
            super().set_tile(new_tile)
        elif (direction == 'u'):
            new_tile = self.my_map.get_up_tile(self.my_tile)
            super().set_tile(new_tile)
        elif (direction == 'd'):
            new_tile = self.my_map.get_down_tile(self.my_tile)
            super().set_tile(new_tile)
        else: raise(RuntimeError())

