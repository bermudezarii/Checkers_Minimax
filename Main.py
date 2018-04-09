# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 00:15:14 2018

@author: bermu
"""

from Game import * 
from Checkers import * 


def get_other_player(player_id):
    if (player_id == 1):
        return 2
    elif(player_id == 2): 
        return 1


def main (board_size): 
    print("WELCOME TO DAMAS / CHECKERS")
    strings = [] 
    player1 = Game(Board(6))
    id_player = 1 
    for i in range(len(player1.board.board)):
        print("perros")
        player1.sprout(id_player)
        

    while (player1.board.board not in strings): 
        print("ovejas")
        
        strings.append(player1.board.board) ## al tablero
        player1 = player1.get_move(id_player)
        id_player = get_other_player(id_player)
        player1.sprout(id_player)
    print(player1.board)
    print("Game over")


main(8)