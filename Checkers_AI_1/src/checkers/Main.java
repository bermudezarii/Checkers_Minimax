package checkers;

import java.awt.event.*;
import java.awt.*;
import javax.swing.*;
import java.util.*;
import java.util.Scanner;
import java.util.ArrayList; 

public class Main extends JPanel implements KeyListener, FocusListener{

    public long sleepTime;

  
    
    
    public static void main(String[] args) {
        System.out.println("Welcome to Checkers");

        LinkedList <String> records = new LinkedList <String> ();
        Random rand = new Random();

        GameTreeNode RED = new GameTreeNode(new BoardPosition());  //the player (incidentally, both players)
        for(int a = 0; a < 8; a ++){
            RED.sprout(true);
        }

        boolean player1 = true;
        while(!RED.BP.gameOver(player1) && !records.contains(RED.BP.toString())){
            System.out.println("not GameOver of " + player1);
            System.out.println(RED.BP);
            records.add(RED.BP.toString());

            RED = RED.getMove(player1);  //tell red to become the next node down in its minimax list
            ArrayList<Integer> moves  =  RED.move_user();
            System.out.println(moves);
            player1 = !player1;
            RED.sprout(player1);
        }
        String winner = ""; 
        System.out.println(RED.BP);
         if(!player1){
            winner = "Player 1";
         }
         else{
             winner = "Player 2";
         }
        System.out.println("Winner: " + winner);
        
    }

    
    public Main(long sleepTime, int width, int height){
        this.sleepTime = sleepTime;
    }

    @Override
    public void paintComponent(Graphics g){
        setBackground(Color.WHITE);
        super.paintComponent(g);

        if(sleepTime >= 0){
            double screenDimensions[] = {getWidth(), getHeight()};
            try{
            }catch(Exception e){System.out.println("Exception: " + e);}
            g.setColor(Color.BLACK);
            g.drawString("" + sleepTime, 0, 10);
        }

        repaint();

        try{Thread.sleep(sleepTime);}catch(Exception e){}
    }
    public String display_player(boolean player){
        if(player){
            return "Player 1";
         }
        return "Player 2";
    }
    
    public void keyTyped(KeyEvent e){}
    public void keyPressed(KeyEvent e){
        //they pressed a key
        if(e.getKeyCode() == KeyEvent.VK_W){  //pressed the W key
            sleepTime ++;  //increment the sleep time
        }
        else if(e.getKeyCode() == KeyEvent.VK_S){  //pressed the S key
            sleepTime --;
        }
    }
    public void keyReleased(KeyEvent e){}
    public void focusLost(FocusEvent e){}
    public void focusGained(FocusEvent e){}
    
   
}
