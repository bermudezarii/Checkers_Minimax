package checkers;

import java.util.LinkedList;

public class BoardPosition {
    public int[][] board;  //the usable squares on the board  0 is open, 1 is player 1, -1 is player 2, K is 1 or -1 * 2

    public BoardPosition(){
        board = new int[8][8];
        for(int a = 0; a < board.length; a++){
            for(int b = 0; b < board[0].length; b++){
                if(b < 3 && (b + a) % 2 == 0){
                    board[a][b] = 1;
                }
                else if(b > 4 && (b + a)%2 == 0){
                    board[a][b] = -1;
                }
                else{
                    board[a][b] = 0;
                }
            }
        }
    }

    
    public BoardPosition(BoardPosition BP, int A, int B, int code){
        board = new int[8][8];
        for(int a = 0; a < board.length; a++){
            for(int b = 0; b < board[0].length; b++){
                board[a][b] = BP.board[a][b];  //copy it over
            }
        }
        int value = board[A][B];
        board[A][B] = 0;
        switch(code){
            case(0): A --;
                     B ++; break; //step right up
            case(1): A ++;
                     B ++; break; //step right down
            case(2): //jump right up
                     board[A-1][B+1] = 0;  
                     A -= 2;
                     B += 2; break;
            case(3): //jump right down
                     board[A+1][B+1] = 0;
                     A += 2;
                     B += 2; break;
            case(4): A --;
                     B --; break; //step right up
            case(5): A ++;
                     B --; break; //step right down
            case(6): //jump right up
                     board[A-1][B-1] = 0;
                     A -= 2;
                     B -= 2;  break;
            case(7): //jump right down
                     board[A+1][B-1] = 0;
                     A += 2;
                     B -= 2;  break;
            default: break;
        }
        board[A][B] = value;
        if((B == 0 && value == -1) || (B == 7 && value == 1)){  //king it
            board[A][B] *= 2;
        }
    }

    public boolean gameOver(boolean player1){
        LinkedList <BoardPosition> moves = getMoves(player1);
        //System.out.println(moves.toString());
        return moves.isEmpty(); 
    }

    
    public LinkedList <BoardPosition> getMoves(boolean player1){
        LinkedList <BoardPosition> moves = new LinkedList <BoardPosition> ();

        for(int a = 0; a < board.length; a++){
            for(int b = 0; b < board[0].length; b++){
                if((player1 && board[a][b] > 0) || (!player1 && board[a][b] < 0)){
                    moves.addAll(getJumpMoves(a, b, board[a][b]));
                }
            }
        }

        if(moves.isEmpty()){  //only add step moves if there are no killing moves
            for(int a = 0; a < board.length; a++){
                for(int b = 0; b < board[0].length; b++){
                    if(player1 && board[a][b] > 0){
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
                    }
                    if(!player1 && board[a][b] < 0){
                        if(open(a-1, b-1)){  //move left and up is open
                            moves.add(new BoardPosition(this, a, b, 4));
                        }
                        if(open(a+1, b-1)){  //move leftt and down is open
                            moves.add(new BoardPosition(this, a, b, 5));
                        }
                        if(board[a][b] == -2){
                            if(open(a-1, b+1)){  //move right and up is open
                                moves.add(new BoardPosition(this, a, b, 0));
                            }
                            if(open(a+1, b+1)){  //move right and down is open
                                moves.add(new BoardPosition(this, a, b, 1));
                            }
                        }
                    }
                }
            }
        }

        return moves;
    }

    
    public LinkedList <BoardPosition> getJumpMoves(int a, int b, int peiceType){
        LinkedList <BoardPosition> moves = new LinkedList <BoardPosition> ();
        if(peiceType > 0 || peiceType == -2){
            if(jumpOK(a, b, a-1,b+1)){
                BoardPosition newBP = new BoardPosition(this, a, b, 2);
                moves.add(newBP);
                moves.addAll(newBP.getJumpMoves(a-2,b+2,peiceType));  //add all the jump moves from this jump move
            }
            if(jumpOK(a, b, a+1,b+1)){
                BoardPosition newBP = new BoardPosition(this, a, b, 3);
                moves.add(newBP);
                moves.addAll(newBP.getJumpMoves(a+2,b+2,peiceType));  //add all the jump moves from this jump move
            }
        }
        if(peiceType < 0 || peiceType == 2){
            if(jumpOK(a, b, a-1,b-1)){
                BoardPosition newBP = new BoardPosition(this, a, b, 6);
                moves.add(newBP);
                moves.addAll(newBP.getJumpMoves(a-2,b-2,peiceType));  //add all the jump moves from this jump move
            }
            if(jumpOK(a, b, a+1,b-1)){
                BoardPosition newBP = new BoardPosition(this, a, b, 7);
                moves.add(newBP);
                moves.addAll(newBP.getJumpMoves(a+2,b-2, peiceType));  //add all the jump moves from this jump move
            }
        }

        return moves;
    }

    
    public boolean jumpOK(int a1, int b1, int a2, int b2){
        return open(2*a2 - a1, 2*b2 - b1) && inBounds(a2, b2) && (Math.signum(board[a2][b2]) == -Math.signum(board[a1][b1]));
    }

    public boolean open(int a, int b){
        return inBounds(a,b) && board[a][b] == 0;
    }

    public boolean inBounds(int a, int b){
        return a >= 0 && a < board.length && b >= 0 && b < board[0].length;
    }

    public int boardValue(){
        int peiceDifference = 0;
        for(int a = 0; a < board.length; a++){
            for(int b = 0; b < board[0].length; b++){
                peiceDifference += board[a][b];
            }
        }
        return peiceDifference;
    }

    @Override
    public String toString(){ // paints the boaard 
        String s = "board: ";
        for(int i = 0; i < board.length; i++){
            s += "\n";
            for(int j = 0; j < board[0].length; j++){
                switch(board[i][j]){
                    case(-2): s += 'B'; break;
                    case(-1): s += 'b'; break;
                    case(0): s +=  "\u25A0"; break;
                    case(1): s += 'r'; break;
                    case(2): s += 'R'; break;
                    default: break;
                }
                s += " ";
            }
        }
        return s;
    }
}
