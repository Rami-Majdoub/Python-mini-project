from actor import Actor
from block import Block

class MovingActor(Actor):
    DIRECTION_UP = 'u'
    DIRECTION_LEFT = 'l'
    DIRECTION_RIGHT = 'r'
    DIRECTION_DOWN = 'd'
    
    def __init__(self, my_map, tile, health, is_enemy):
        super().__init__(my_map, tile, health, is_enemy)

    # block, door, enemy, player, potion
    def check_constraint(self, current_tile, new_tile):
        if new_tile.contains_block(): return False
        if current_tile.contains_enemy():
            if new_tile.contains_enemy() or new_tile.contains_door(): return False
        return True
        
    def can_go_left(self):
        current_tile = super().get_tile()
        new_tile = self.my_map.get_left_tile(current_tile)
        if (new_tile == None): # there is no tile on my left
            return False
        else:
            return self.check_constraint(current_tile, new_tile)
        
    def can_go_right(self): 
        current_tile = super().get_tile()
        new_tile = self.my_map.get_right_tile(current_tile)
        if (new_tile == None):
            return False # there is no tile on my right
        else: 
            return self.check_constraint(current_tile, new_tile)
            
    def can_go_up(self): 
        current_tile = super().get_tile()
        new_tile = self.my_map.get_up_tile(current_tile)
        if (new_tile == None):
            return False # there is no tile on my up
        else:
            return self.check_constraint(current_tile, new_tile)
            
    def can_go_down(self):
        current_tile = super().get_tile()
        new_tile = self.my_map.get_down_tile(current_tile)
        if (new_tile == None):
            return False # there is no tile on my down
        else:
            return self.check_constraint(current_tile, new_tile)

    def get_possible_moves(self):
        moves = []
        if self.can_go_left(): moves.append(MovingActor.DIRECTION_LEFT)
        if self.can_go_right(): moves.append(MovingActor.DIRECTION_RIGHT)
        if self.can_go_up(): moves.append(MovingActor.DIRECTION_UP)
        if self.can_go_down(): moves.append(MovingActor.DIRECTION_DOWN)
        return moves

    def __unattach_from_current_tile(self):
        super().get_tile().set_actor(None)
        super().set_tile(None)

    def __attach_to_tile(self, new_tile):
        new_tile.set_actor(self)
        super().set_tile(new_tile)

    def move_to_new_tile(self, new_tile):
        current_tile = super().get_tile()
        
        # player or enemy getting potion
        if new_tile.contains_potion() and (current_tile.contains_enemy() or current_tile.contains_player()):
            potion = new_tile.get_actor()
            current_tile.get_actor().increase_health(potion.get_health())

            potion.die()
            self.__unattach_from_current_tile()
            self.__attach_to_tile(new_tile)
            return True
            
        # enemy attacking player
        if (current_tile.contains_enemy() and new_tile.contains_player()) :
            player = new_tile.get_actor()
            enemy = current_tile.get_actor()
            print('enemy attack! health: {}'.format(enemy.get_health()))
            player.decrease_health(enemy.get_health())
            
            enemy.die()
            self.__unattach_from_current_tile()
            return True
            
        # player attacking enemy
        if (current_tile.contains_player() and new_tile.contains_enemy()) :
            player = current_tile.get_actor()
            enemy = new_tile.get_actor()
            player.decrease_health(enemy.get_health())

            enemy.die()
            self.__unattach_from_current_tile()
            self.__attach_to_tile(new_tile)
            return True

        # player door
        if (current_tile.contains_player() and new_tile.contains_door()) :
            player = current_tile.get_actor()
            door = new_tile.get_actor()

            door.die()
            self.__unattach_from_current_tile()
            self.__attach_to_tile(new_tile)
            return True
        
        self.__unattach_from_current_tile()
        self.__attach_to_tile(new_tile)
        return True

    def move(self, direction):
        if (direction == MovingActor.DIRECTION_LEFT):
            new_tile = self.my_map.get_left_tile(self.my_tile)
            self.move_to_new_tile(new_tile)
            
        elif (direction == MovingActor.DIRECTION_RIGHT):
            new_tile = self.my_map.get_right_tile(self.my_tile)
            self.move_to_new_tile(new_tile)
            
        elif (direction == MovingActor.DIRECTION_UP):
            new_tile = self.my_map.get_up_tile(self.my_tile)
            self.move_to_new_tile(new_tile)
            
        elif (direction == MovingActor.DIRECTION_DOWN):
            new_tile = self.my_map.get_down_tile(self.my_tile)
            self.move_to_new_tile(new_tile)
        else: raise(RuntimeError())

