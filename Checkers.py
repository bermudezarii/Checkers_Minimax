# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 01:27:14 2018

@author: bermu
"""
#prueba jaja
import numpy as np
np.set_printoptions(threshold=np.nan)



class board: 
    board = [] 
    
    def __init__(self, size = 8, board1 = [], i = None, j = None, code = None): 
        if (board1 == []): 
            board = init_board(size)
        else: 
            self.board = board1 
        if i is not None and j is not None and code is not None: 
            value = board[i,j]
            self.board[i,j] = 0
            row_dir = code[0]
            col_dir = code[1]
            jump = code[2]
            
            if (jump == 1): ## +2 or -2 cuz jump
                if (row_dir == 1): ## up
                    i -= 2
                else:
                    i += 2          ## down 
                if (col_dir == -1):
                    j -= 2          ## left
                else: 
                    j += 2          ## right
            else:           ## +1 or - 1 cuz normal move
                if (row_dir == 1): ## up
                    i -= 1
                else:
                    i += 1          ## down 
                if (col_dir == -1):
                    j -= 1          ## left
                else: 
                    j += 1          ## right 
            self.board[i,j] = value
            if ((j == 0 and value == 2 ) or (j == len(self.board)-1 and value == 1 )): 
                self.board[i,j] += 2


    def get_normal_moves(self, player):
        moves = []
        for i in range(len(board)): 
            for j in range(len(board[0])): 
                if (((player == 1 or player == 3) and (board[i,j] == 1 or board[i,j] == 3)) or 
                ((player == 2 or player == 4) and (board[i,j] == 2 or board[i,j] == 4))): 
                    moves.extend(get_jump_moves(i, j, board[i,j]))
        if (len(moves) == 0): ## will only have step moves
            for i in range(len(board)): 
                for j in range(len(board[0])): 
                    if ((player == 1 or player == 3) and (board[i,j] == 1 or board[i,j] == 3)):
                        if (valid_open_pos(i-1, j+1)): 
    ##                        moves.append(generateBoard(board))
            
        return moves
                

    def get_jump_moves(self, i, j, player_type):
        moves = []
        
        if (player_type == 1 || player_type == 3 || player_type == 4): #piece moves to the same direction, player 1 or queen player 2
            if(possible_jump(i, j, i-1,j+1)):
                new_board = board(self, i, j, 2)
                moves.append(new_board)
                moves.extend(new_board.get_jump_moves(i-2,j+2, player_type)) #add all the jump moves from this jump move

            if(possible_jump(i, j, i+1,j+1):
               new_board = board(self, i, j, 3)
               moves.append(new_board)
               moves.extend(new_board.get_jump_moves(i+2,j+2, player_type)) #add all the jump moves from this jump move

        if (player_type == 2 || player_type == 4 || player_type == 3): #piece moves to the same direction, player 2 or queen player 1
            if(possible_jump(i, j, i-1,j-1)):
               new_board = board(self, i, j, 6)
               moves.append(new_board)
               moves.extend(new_board.get_jump_moves(i-2,j-2, player_type)) #add all the jump moves from this jump move
               
            if(possible_jump(i, j, i+1,j-1)):
               new_board = board(self, i, j, 7)
               moves.append(new_board)
               moves.extend(new_board.get_jump_moves(i+2,j-2, player_type)) #add all the jump moves from this jump move
               
        return moves

           
    def get_other_player(self, player_id):
        if (player_id == 1 or player_id == 3):
            return [2, 4]
        elif(player_id == 2 or player_id == 4): 
            return [1, 3]


    def possible_jump(self, i1, j1, i2, j2): 
        further_i = 2 * i2 - i1 
        further_j = 2 * j2 - j1 
        other_player = get_other_player(board[i1,j1])
        ##we check that further is valid and the middle guy its from the other player 
        ## so it can be eaten 
        return (valid_open_pos(further_i, further_j) and (board[i2,j2] == other_player[0] or board[i2,j2] == other_player[1]))


    def valid_open_pos(self, i, j): 
        return (exist_position(i,j) and board[i,j] == 0)


    def exist_position(self, i, j): 
        ## checks if i is inside the rows length and same with j and columns also if 
        ## space is 0 because thats valid the -1 aren't 
        return (i >= 0 and  i < len(board) and j >= 0 and len(board[0]))


    def get_normal_moves(self, player):
        moves = []
        for i in range(len(self.board)): 
            for j in range(len(self.board[0])): 
                if (((player == 1 or player == 3) and (self.board[i,j] == 1 or self.board[i,j] == 3)) or 
                ((player == 2 or player == 4) and (self.board[i,j] == 2 or self.board[i,j] == 4))): 
                    moves.extend(get_jump_moves(i, j, self.board[i,j]))
        if (len(moves) == 0): ## will only have step moves
            for i in range(len(self.board)): 
                for j in range(len(self.board[0])): 
                    if ((player == 1 or player == 3) and (self.board[i,j] == 1 or self.board[i,j] == 3)):
                        if (valid_open_pos(i-1, j+1)):      ## right and up 
                            moves.append(board(self, i, j, [1, 1, 0]))
                        if (valid_open_pos(i+1, j+1)):      ##  right and down
                            moves.append(board(self, i, j, [-1, 1, 0]))
                        if (self.board[i,j] == 3):
                            if (valid_open_pos(i-1, j-1)):  ##  left and up 
                                moves.append(board(self, i, j, [1, -1, 0]))
                            if (valid_open_pos(i+1, j-1)):  ##  left and down
                                moves.append(board(self, i, j, [-1, -1, 0]))
                     if ((player == 2 or player == 4) and (self.board[i,j] == 2 or self.board[i,j] == 4)):
                        if (valid_open_pos(i-1, j-1)):      ## left and up
                            moves.append(board(self, i, j, [1, -1, 0]))
                        if (valid_open_pos(i+1, j-1)):      ## left and down 
                            moves.append(board(self, i, j, [-1, -1, 0]))
                        if (self.board[i,j] == 4):
                            if (valid_open_pos(i-1, j+1)):  ##  right and up
                                moves.append(board(self, i, j, [1, 1, 0]))
                            if (valid_open_pos(i+1, j-1)):  ##  right and down
                                moves.append(board(self, i, j, [-1, 1, 0]))
        return moves


    def board_value():
        piece_difference = 0
        for i in range(len(self.board)):
            for j in range (len(board[0])):
                piece_difference += board[a][b]
        return piece_difference
    

def main (board_size): 
    init_board(board_size)


main(8)
