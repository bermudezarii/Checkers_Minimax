# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 01:27:14 2018

@author: bermu
"""
import numpy as np
np.set_printoptions(threshold=np.nan)

board = []


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





def valid_position(i, j): 
    ## checks if i is inside the rows length and same with j and columns also if 
    ## space is 0 because thats valid the -1 aren't 
    return (i >= 0 and  i < len(board) and j >= 0 and len(board[0])) and board[i,j] == 0 

def main (board_size): 
    init_board(board_size)


main(8)