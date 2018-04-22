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
  
