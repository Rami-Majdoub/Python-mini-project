import os
import time

from map import Map
from player import Player
from enemy import Enemy
from block import Block
from potion import Potion
from door import Door
from levelGenerator import LevelGenerator

from random import *

def printGame(console, my_map, potions, player):
    if console: os.system('cls')
    my_map.show()
    for p in potions:
        if not p.is_dead(): print(p)
    print(player)
    
if __name__ == '__main__':
    console = True #
    level_generator = LevelGenerator(columns = 10, rows = 10, nb_blocks = 4, nb_enemies = 20, nb_potions = 2)
    
    my_map = level_generator.get_map()
    player = level_generator.get_player()
    door = level_generator.get_door()
    
    enemies = level_generator.get_enemies()
    blocks = level_generator.get_blocks()
    potions = level_generator.get_potions()

    while (not player.is_dead()):
        if not console: print()
        printGame(console, my_map, potions, player)
        
        moves = player.get_possible_moves()
        while True:
            print()
            move = input('choose next move {}: '.format(moves).replace("'", "") ) # remove str quotes
            #move = moves[0] # for debugging
            if move in moves: break
            
        player.move(move)
        if player.is_dead() or door.is_dead(): break
        
        for e in enemies:
            if not e.is_dead():
                # enemy will choose to move or to stay still
                enemy_will_move = random() < 0.5
                if not enemy_will_move: continue
                e.move()

                printGame(console, my_map, potions, player)
                if console: time.sleep(1)
                
                if player.is_dead(): break # enemy killed player
        
    if player.is_dead(): print('you died')
    elif door.is_dead(): print('level completed')
    input()
