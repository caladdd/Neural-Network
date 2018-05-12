#!/usr/bin/python3
import math 

def sigmoid(x):
	return 1/(1+math.exp(-x))


class Neuron:
	def __init__(self,n):
		self.id = n
		self.z = 0
		self.a = sigmoid(self.z)
		self.bias = 0

	def __str__(self):
		return "( a:"+str((int(self.a*100))/100)+" )"

	@property
	def z(self): return self.__z

	@z.setter
	def z(self,n):
		self.a = sigmoid(n)
		self.__z = n

class Layer:
	def __init__(self,numNeurons,numNeuronsNext=0):
		self.listNeurons = []
		self.listW = []
		for i in range(numNeurons):
			self.listNeurons.append(Neuron(i))
			listaA = [1 for j in range(numNeuronsNext)]
			self.listW.append(listaA)

	def __str__(self):
		string = ""
		for i in self.listNeurons:
			string += str(i)+" "
		return string

class Net:
	def __init__(self,listNumLayer):
		self.listLayer = [ Layer(listNumLayer[0]) ]
		for i in range(len(listNumLayer)-1):
			self.listLayer.append(Layer(listNumLayer[i+1],listNumLayer[i]))
	
	def __str__(self):
		string = ""
		for i in self.listLayer:
			string += str(i)+"\n"
			#string += str(i.listW)+"\n"	
		return string

	def calculate(self,initalValues):
		# Setting initial values
		for indexValue in range(len(initalValues)):
			self.listLayer[0].listNeurons[indexValue].a = initalValues[indexValue]
		# Calculating 
		for indexLayer in range(len(self.listLayer)-1): # Iteration in layers: it starts since 2
			length = len(self.listLayer[indexLayer+1].listNeurons)
			for indexNeuron in range(length): # Iteration in Neurons
				acum = 0
				for i in range(len(self.listLayer[indexLayer].listNeurons)): # Iteration in a*w
					a = self.listLayer[indexLayer].listNeurons[i].a
					w = self.listLayer[indexLayer+1].listW[indexNeuron][i]
					acum += a*w
				bias = self.listLayer[indexLayer+1].listNeurons[indexNeuron].bias 
				self.listLayer[indexLayer+1].listNeurons[indexNeuron].z = acum + bias
		# Final values
		finalList = []
		for finalNeuron in self.listLayer[-1].listNeurons:
			finalList.append(finalNeuron.a)
		return finalList

class Trainer:
	def __init__(self,neuralNetwork):
		self.net = neuralNetwork

	def dC_dbWjk(self,l,j,k):
	def dC_dBlj(self,l,j):
	def dC_dAljk(self,l,j,k):

	def train(self,initialValues,finalValues):
		estimatedValues = self.net.calculate(initialValues)

	def backPropagation(self,inputList,outputList):
		print("Net has started.")
		for i in range(len(inputList)):
			print("Net is learning...")
			train(inputList[i],outputList[i])
		print("Net has finished.")


			







a = Net([3,4,3,2])
print(a)
l = a.calculate([12,23,13])
print(a)
print("")
print(l)

