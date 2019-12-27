from map import Map
from player import Player

if __name__ == '__main__':
    my_map = Map()
    my_map.generate_new()
    my_map.show()

    player = Player(my_map, my_map.get_empty_tile(), 10)

    while (player != None):
        my_map.show()
        moves = player.get_possible_moves()
        while True:
            move = input('choose next move {}: '.format(moves) )
            if move in moves: break
        player.move(move)
