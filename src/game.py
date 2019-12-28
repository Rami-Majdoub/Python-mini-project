from map import Map
from player import Player
from enemy import Enemy
from block import Block
from potion import Potion
from door import Door

if __name__ == '__main__':
    my_map = Map()
    
    player = Player(my_map)
    enemy = Enemy(my_map)
    block = Block(my_map)
    potion = Potion(my_map)
    door = Door(my_map)

    while (not player.is_dead() and not door.is_dead()):
        my_map.show()
        moves = player.get_possible_moves()
        while True:
            print()
            move = input('choose next move {}: '.format(moves).replace("'", "") ) # remove str quotes
            if move in moves: break
            
        player.move(move)
        if(not enemy.is_dead()): enemy.move()
        print()
    if player.is_dead(): print('you died')
    elif door.is_dead(): print('level completed')
