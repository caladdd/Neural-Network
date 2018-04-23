import math

class Neuron:
    def __init__(self):
        self.bias = 0
        self.lPrev = []
        self.lNext = []
        self.value = 0

    def __str__(self):
        return "("+str(self.value)+")"
        
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

    def __str__(self):
        string = ""
        for layer in self.schema:
            for neuron in layer:
                string += str(neuron)+" "
            string+="\n"
        return string
    
    def addLayer(self,neurons,weightList):
        indexWeight = 0 
        for lastNeuron in self.lastNeurons:
            for neuron in neurons:
                lastNeuron.addConection(weightList[indexWeight],neuron)
                neuron.addConectionI(weightList[indexWeight],lastNeuron)
                indexWeight += 1
        self.lastNeurons = neurons
        self.schema.append(neurons)
        self.countLayers += 1 
  

def main():
    n1 = InitialNeuron(0.1)
    n2 = InitialNeuron(0.5)
    n3 = InitialNeuron(0.222)

    neurons = [n1, n2, n3]
    net = Net(neurons)
    print("Se ha creado una red")
    
    n4 = Neuron()
    n4.setBia(0.6)
    n5 = Neuron()
    n5.setBia(0.65)
    n6 = Neuron()
    n6.setBia(0.98)
    n7 = Neuron()
    n7.setBia(0.2)
    neurons = [n4,n5,n6,n7]
    weights = [2,3,2,3,1,4,1,4,6,7,6,7]
    net.addLayer(neurons,weights)
    print("Se ha agregado una capa nueva")

    n8 = Neuron()
    n8.setBia(0.8)
    n9 = Neuron()
    n9.setBia(0.556)
    neurons = [n8,n9]
    weights = [1,5,9,3,8,5,7,6]
    net.addLayer(neurons,weights)

    print(net)
    
main()
