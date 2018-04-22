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
        # Temporaly
        self.value = value
