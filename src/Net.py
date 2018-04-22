class Neuron:
    def __init__(self):
        self.bias = 0
        self.lPrev = []
        self.lNext = []
        self.value = 0

    def addConection(self,weight,neuron):
        self.lNext.append((weight,neuron))

    def addConectionI(self,weight,neuron):
        self.lPrev.append((weight,neuron))

    def setBia(self,b):
        self.bias = b

    def calculateValue(self):
        # Temporally
        self.value = value

        
class InitialNeuron(Neuron):
    def __init__(self,initialValue):
        Neuron.__init__(self)
        self.value = initialValue 
        
    def setValue(self,num): 
        sefl.value = num

        
class Net:
    def __init__(self,neurons):
        self.countLayers = 1
        self.schema = [neurons] 
        self.initialNeurons = neurons
        self.lastNeurons = neurons

    def addLayer(self,neurons,weightList):
        indexWeight = 0 
        for lastNeuron in self.lastNeurons:
            for neuron in neurons:
                lastNeuron.addConection((weightList[indexWeight],neuron))
                neuron.addConectionI((weightList[indexWeight],lastNeuron))
                indexWeight += 1
        self.lastNeurons = neurons
        self.schema.append(neurons)
        self.countLayers += 1 
  

def main():
    n1 = InitialNeuron(0.1)
    n2 = InitialNeuron(0.5)
    n3 = InitialNeuron(0.222)

    neurons = [n1, n2, n3]
    print("Se crearon las neuronas iniciales")

    net = Net(neurons)
    n4 = Neuron()
    n5 = Neuron()
    n6 = Neuron()
    n7 = Neuron()
    neurons = [n4,n5,n6,n7]
    

main()
