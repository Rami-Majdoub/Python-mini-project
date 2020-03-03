from movingActor import MovingActor
from random import *

class Enemy(MovingActor):
    
    presentation = '*'

    def __init__(self, my_map, tile = None, health = 1):
        super().__init__(my_map, tile, health, True)

    def show(self):
        print(' {} '.format(Enemy.presentation), end='')

    def move(self):
        possible_moves = super().get_possible_moves() # Left, Right, Up, Down
        if len(possible_moves) == 0: return None # can't move: blocked
        # pass error
        # chosen_move_index = randrange( len(possible_moves) )
        # File "C:\Users\W.S.I\AppData\Local\Programs\Python\Python37\lib\random.py", line 190, in randrange
        # raise ValueError("empty range for randrange()")
        # ValueError: empty range for randrange()
        
        chosen_move_index = randrange( len(possible_moves) )
        # chosen_move_index = randint(0,  len(possible_moves)-1 )
        
        chosen_move = possible_moves[chosen_move_index]
        super().move(chosen_move)
