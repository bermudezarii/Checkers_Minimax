def paint_board(board):
    try:
        switcher = {
            4: "B",
            2: "b",
            0: "_",
            -1: u"\u25A0",
            1: "r",
            3: "R"
        }
        for i in range(8):
            for j in range(8):
    
                print (switcher.get(board[i][j]), " ", end="", flush=True)
    
            print("")
        print("\n\n")
    except: 
        print(board)
            
board = [[1, -1, 1, -1, 1, -1, 1, -1],
         [-1, 1, -1, 1, -1, 1, -1, 1],
         [1, -1, 1, -1, 1, -1, 1, -1],
         [-1, 0, -1, 0, -1, 0, -1, 0],
         [0, -1, 0, -1, 0, -1, 0, -1],
         [-1, 2, -1, 2, -1, 2, -1, 2],
         [2, -1, 2, -1, 2, -1, 2, -1],
         [-1, 2, -1, 2, -1, 2, -1, 2],
         [2, -1, 2, -1, 2, -1, 2, -1]
         ]

paint_board(board)

                
