# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 23:35:50 2018

@author: bermu
"""

class Game: 
    children = []
    board = [] 
    
    def __init__(self, board): 
        self.board = board 
        
    def sprout(self, id_player): 
        for child in self.children: 
            child.sprout(self.get_other_player)
        
        if(self.children == []): 
            moves = self.board.get_normal_moves(id_player)
            for board_ in moves: 
                self.children.append(Game(board_))
        
    def minimax(self, id_player): 
        if(self.children == []):
            return self.board.board_value()
        if(id_player == 1): 
            max_ = float('-inf')
            for child in self.children: 
                max_ = max(max_, child.minimax(self.get_other_player))
            return max_ 
        else: 
            min_ = float('inf')
            for child in self.children: 
                min_ = min(min_, child.minimax(self.get_other_player))
            return min_
        
        
    def get_move(self, id_player): 
        if (self.children == []): 
            return None 
        best = None 
        max_score = 0
        if (id_player == 1): 
            max_score = float('-inf') 
        else: 
            max_score = float('inf')     
        for child in self.children:
            value = child.minimax(id_player)
            minimax_sign = 0 
            if (id_player == 1): 
                minimax_sign = 1 
            else: 
                minimax_sign = -1         
            if (best is None or (value*minimax_sign > max_score*minimax_sign)): 
                max_score = value 
                best = child
        return best 
        