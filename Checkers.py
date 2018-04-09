# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 01:27:14 2018

@author: bermu
"""
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
                if (row_dir == -1): ## up
                    i -= 2
                else:
                    i += 2          ## down 
                if (col_dir == -1):
                    j -= 2          ## left
                else: 
                    j += 2          ## right
            else:           ## +1 or - 1 cuz normal move
                if (row_dir == -1): ## up
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
        


def even(num):
    if (num % 2 == 0): 
        return True
    else: 
        return False

def init_board(size):
    s = (size, size)
    board = np.zeros(s)
    for i in range(size):
        for j in range(size):    
            if((even(i)==False and even(j)) or (even(i) and even(j) == False)): 
                board[i,j] = -1
            elif(( i == 0 or i == 1 or i == 2 ) and ((even(i) and even(j)) or (even(i) ==0 and even(j) ==0))):
                 board[i,j] = 1
            elif(( i == size-1 or i == size-2 or i == size-3 ) and ((even(i) and even(j)) or (even(i)==0 and even(j)==0))):
                 board[i,j] = 2 
    print(board)
    return board



def get_normal_moves(player):
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
                        moves.append(generateBoard(board))
        
        
                        if(open(a-1, b+1)){  //move right and up is open
                            moves.add(new BoardPosition(this, a, b, 0));
                        }
                        if(open(a+1, b+1)){  //move right and down is open
                            moves.add(new BoardPosition(this, a, b, 1));
                        }
                        if(board[a][b] == 2){
                            if(open(a-1, b-1)){  //move left and up is open
                                moves.add(new BoardPosition(this, a, b, 4));
                            }
                            if(open(a+1, b-1)){  //move leftt and down is open
                                moves.add(new BoardPosition(this, a, b, 5));
                            }
                        }
                    
        
        
    return moves
            


def get_other_player(player_id):
    if (player_id == 1 or player_id == 3):
        return [2, 4]
    elif(player_id == 2 or player_id == 4): 
        return [1, 3]

def possible_jump(i1, j1, i2, j2): 
    further_i = 2 * i2 - i1 
    further_j = 2 * j2 - j1 
    other_player = get_other_player(board[i1,j1])
    ##we check that further is valid and the middle guy its from the other player 
    ## so it can be eaten 
    return (valid_open_pos(further_i, further_j) and (board[i2,j2] == other_player[0] or board[i2,j2] == other_player[1]))


def valid_open_pos(i,j): 
    return (exist_position(i,j) and board[i,j] == 0)

def exist_position(i, j): 
    ## checks if i is inside the rows length and same with j and columns also if 
    ## space is 0 because thats valid the -1 aren't 
    return (i >= 0 and  i < len(board) and j >= 0 and len(board[0])) 



def main (board_size): 
    init_board(board_size)


main(8)