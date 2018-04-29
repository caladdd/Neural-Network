package Network;

import java.util.LinkedList;

public class Neuron {
	float bia;
	LinkedList<PairNeuWei> lPrev; 
	LinkedList<PairNeuWei> lNext;
	
	public Neuron(float bia) {
		this.bia=bia;
	}
	
	public void addConnection(float weight, Neuron net) {
		PairNeuWei temp = new PairNeuWei(net,weight);
		lNext.add(temp);
	}
	
	public void addConnectionI(float weight, Neuron net) {
		PairNeuWei temp = new PairNeuWei(net,weight);
		lPrev.add(temp);
	}
}
