package checkers;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;


public class GameTreeNode {
    public LinkedList <GameTreeNode> children;  //the resulting possible moves
    public BoardPosition BP;  //the associated board position

    public GameTreeNode(BoardPosition BP){
        children = new LinkedList <GameTreeNode> ();
        this.BP = BP;
    }


    public void sprout(boolean player1){
        for(GameTreeNode GTN : children){
            GTN.sprout(!player1);
        }

        if(children.isEmpty()){
            LinkedList <BoardPosition> moves = BP.getMoves(player1);
            for(BoardPosition b : moves){
                children.add(new GameTreeNode(b));  //add them all to the list
            }
        }
    }

     public ArrayList<Integer> move_user(){
         ArrayList<Integer> moves = new ArrayList<Integer>();
         
        Scanner reader = new Scanner(System.in);  // Reading from System.int
        System.out.println("Enter row of piece");
        int n = reader.nextInt(); // Scans the next token of the input as an int.
        moves.add(n); 
        System.out.println("Enter col of piece");
        n = reader.nextInt(); // Scans the next token of the input as an int.
        moves.add(n); 
        System.out.println("Enter new row of piece");
        n = reader.nextInt(); // Scans the next token of the input as an int.
        moves.add(n); 
        System.out.println("Enter new col of piece");
        n = reader.nextInt(); // Scans the next token of the input as an int.
        moves.add(n);         
        reader.close();
        return moves; 
    }
    public double minimax(boolean player1){
        if(children.isEmpty()){  //if this is as deep as it gets
            return BP.boardValue();
        }

        if(player1){  //if it is player1, we maximise the score
            double a = Double.MIN_VALUE; // - infinito
            for(GameTreeNode GTN : children){  //cycle through all of the possible resulting moves
                a = Math.max(a, GTN.minimax(!player1));
            }
            System.out.println("player 1, max score,  a: " + a);
            return a;
        }
        else{   //if it is player 2, we minimize the score
            double a = Double.MAX_VALUE; // + inifity 
            for(GameTreeNode GTN : children){  //cycle through all of the possible resulting moves
                a = Math.min(a, GTN.minimax(!player1));
            }
            System.out.println("player 2, min score, a: " + a);
            return a;
        }
    }

    public GameTreeNode getMove(boolean player1){
        if(children.isEmpty()){
            return null;
        }

        GameTreeNode best = null;
        double maxScore = (player1 ? Double.MIN_EXPONENT : Double.MAX_VALUE);  //highest or lowest, depending on what we want
        for(GameTreeNode GTN : children){
            double value = GTN.minimax(player1);
            if(best == null || value * (player1 ? 1 : -1) > maxScore * (player1 ? 1 : -1)){
                maxScore = value;
                best = GTN;
            }
        }
        
        return best;
    }
}
