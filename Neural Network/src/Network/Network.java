package Network;

import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Network extends JPanel{
    Neuron[][] neuron;
    
    @Override
    public void paintComponent(Graphics g) {
    	super.paintComponent(g);
    	
    	Graphics2D g2d = (Graphics2D) g;

        Dimension size = getSize();

        int w = size.width;
        int h = size.height;  
        System.out.println(w);
    }
    
    
    public void readFile() {
    	//readFile
    }
    
    
    public static void main(String[] args) {
    	JFrame frame = new JFrame("Neural Network");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        int width = 1200;
        int height = 720;
        Network network = new Network();
        
     // Draw the result
        frame.add(network);
        frame.setSize(width, height);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
