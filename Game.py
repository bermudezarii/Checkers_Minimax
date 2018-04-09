# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 23:35:50 2018

@author: bermu
"""
from Checkers import * 
from PaintBoard import *
from copy import copy

class Game: 
    children = []
    board = [] 
    
    def __init__(self, board): 
        self.board = board 
        
    def sprout(self, id_player, depth): 
        if (depth > 0):
            for child in self.children: 
                child.sprout(self.get_other_player(id_player), depth-1)
            
            if(self.children == []): 
                print("juju")
                moves = self.board.get_normal_moves(id_player)
                
                print(moves)
                for board_ in moves: 
                    print("a?")
                    paint_board(board_)
                    self.children.append(Game(board_))
                        
            
    def minimax(self, id_player, depth): 
        if(depth > 0): 
            if(self.children == []):
                return self.board.board_value()
            if(id_player == 1): 
                max_ = float('-inf')
                for child in self.children: 
                    new_child = copy(child)
                    max_ = max(max_, new_child.minimax(self.get_other_player(id_player),  depth-1))
                return max_ 
            else: 
                min_ = float('inf') 
                for child in self.children: 
                    new_child = copy(child)
                    min_ = min(min_, new_child.minimax(self.get_other_player(id_player), depth-1))
                return min_
        return self.board.board_value()
        
        
    def get_move(self, id_player, depth): 
        if (self.children == []): 
            print("1")
            return None 
        best = None 
        print("2")
        max_score = 0
        if (id_player == 1): 
            max_score = float('-inf') 
        else: 
            max_score = float('inf')  
        print(len(self.children))
        for child in self.children:
            print("3")
            value = child.minimax(id_player, depth)
            print("the value: " + str(value))
            minimax_sign = 0 
            if (id_player == 1): 
                minimax_sign = 1 
            else: 
                minimax_sign = -1         
            if (best is None or (value*minimax_sign > max_score*minimax_sign)): 
                print("pfa")
                max_score = value 
                best = child
        return best 
    
    def get_other_player(self, player_id):
        if (player_id == 1 or player_id == 3):
            return [2, 4]
        elif(player_id == 2 or player_id == 4): 
            return [1, 3]

        