from map import Map
from player import Player
from enemy import Enemy

if __name__ == '__main__':
    my_map = Map()
    #my_map.show()

    player = Player(my_map, my_map.get_empty_tile(), 10)
    enemy = Enemy(my_map, my_map.get_empty_tile(), 10)

    while (player != None):
        my_map.show()
        moves = player.get_possible_moves()
        while True:
            move = input('choose next move {}: '.format(moves) )
            if move in moves: break
            
        player.move(move)
        enemy.move()
        print()
