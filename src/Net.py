import math


class Neuron:
    def __init__(self):
        self.bia = 0
        self.lPrev = []
        self.lNext = []
        self.value = 0
        self.needCalculate = True

    def __str__(self):
        return "("+str(self.value)+")"
        
    def addConection(self,weight,neuron):
        self.lNext.append((weight,neuron))

    def addConectionI(self,weight,neuron):
        self.lPrev.append((weight,neuron))

    def setBia(self,b):
        self.bia = b

    def requireCalculate(self):
        self.needCalculate = True
        
    def calculateValue(self):
        if self.needCalculate:
            acum = 0
            for weight,neuron in self.lPrev:
                acum += neuron.calculateValue()*weight 
            acum = self.bia+acum
            #temporally
            self.value = 1/(1+math.exp(-acum))
            self.needCalculate = False
        return self.value


class InitialNeuron(Neuron):
    def __init__(self,initialValue):
        Neuron.__init__(self)
        self.lPrev = None
        self.value = initialValue
        self.needCalculate = False
        
    def setValue(self,num): 
        self.value = num


class Net:
    def __init__(self,neurons):
        self.countLayers = 1
        self.schema = [neurons]
        self.initialNeurons = neurons
        self.lastNeurons = neurons

    def getInitialNeurons(self):
        return self.initialNeurons

    def getLastNeurons():
        return self.lastNeurons

    def __str__(self):
        string = ""
        for layer in self.schema:
            for neuron in layer:
                string += str(neuron)+" "
            string+="\n"
        return string
    
    def addLayer(self,neurons):
        for lastNeuron in self.lastNeurons:
            for neuron in neurons:
                lastNeuron.addConection(1,neuron)
                neuron.addConectionI(1,lastNeuron)
        self.lastNeurons = neurons
        self.schema.append(neurons)
        self.countLayers += 1

    def getOutput(self):
        for i in self.lastNeurons:
            i.calculateValue()

class NetBuilder:
    def buildNet(self,layers):
        neurons = []
        # Initial Neurons
        for i in range(layers[0]):
            neurons.append(InitialNeuron(0))
        net = Net(neurons)
        # Layers
        for layer in layers[1:]:
            neurons = []
            for i in range(layer):
                neurons.append(Neuron())
            net.addLayer(neurons)
        return net

def main():
    netBuilder =  NetBuilder()
    # Creating a Neural Network using a builder
    net = netBuilder.buildNet([3,3,2,3])
    # Setting initial values 
    iniN = net.getInitialNeurons()
    iniN[0].setValue(0.211)
    iniN[1].setValue(0.323)
    iniN[2].setValue(0.888)

    print(net)
    net.getOutput()
    print(net)
main()
