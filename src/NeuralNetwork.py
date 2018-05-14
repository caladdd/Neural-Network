#!/usr/bin/python3
from copy import copy
import math 

def sigmoid(x):
	return 1/(1+math.exp(-x))

def dSigmoid(x):
	return math.exp(x)/(1+math.exp(x))**2


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
			listaA = [0 for j in range(numNeuronsNext)]
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
			string += str(i.listW)+"\n"	
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

	def dC_dWljk(self,l,j,k,y,initial=False):
		# dZlj_dWljk 
		acum = self.net.listLayer[l-1].listNeurons[k].a
		# dAlj_dAlj
		zlj = self.net.listLayer[l].listNeurons[j].z
		acum *= dSigmoid(zlj)
		# dC_dAlj
		if(initial):
			alj = self.net.listLayer[l].listNeurons[j].a
			acum *= 2*(alj-y)**2
		else:
			acum *= y 
		return acum


	def dC_dBlj(self,l,j,y,initial=False):
		#dZlj_dBlj = 1
		acum = 1
		#dAlj_dAlj
		zlj = self.net.listLayer[l].listNeurons[j].z
		acum *= dSigmoid(zlj)
		#dC_dAlj
		if(initial):
			alj = self.net.listLayer[l].listNeurons[j].a
			acum *= 2*(alj-y)**2
		else:
			acum *= y 
		return acum


	def dC_dAljk(self,l,k,vector_y,initial=False):
		acum = 0
		for j in range(len(self.net.listLayer[l].listNeurons)):
			# dZlj_dAl-1k
			acum1 = self.net.listLayer[l].listW[j][k]
			# dAlj_dZlj
			acum1  *=  self.net.listLayer[l].listNeurons[j].z
			# dC_dZlj
			if(initial):
				alj = self.net.listLayer[l].listNeurons[j].a
				acum1 *= 2*(alj-vector_y[j])**2
			else:
				acum1 *= vector_y[j]
			acum += acum1
		return acum


	def train(self,initialValues,finalValues):
		h = 1
		indexLastLayer = len(self.net.listLayer)-1
		estimatedValues = self.net.calculate(initialValues)
		netc = copy(self.net)
		#last layer
		for j in range(len(self.net.listLayer[-1].listNeurons)):
			# New bias
			x =  h*self.dC_dBlj(indexLastLayer,j,finalValues[j],True)
			netc.listLayer[-1].listNeurons[j].bias = self.net.listLayer[-1].listNeurons[j].bias - x
			# New Weights 
			for k in range(len(self.net.listLayer[-2].listNeurons)):
				x = h*self.dC_dWljk(indexLastLayer,j,k,finalValues[j],True)
				netc.listLayer[-1].listW[j][k] = self.net.listLayer[-1].listW[j][k] - x
		# New finalValues
		finalValues1 = []
		for k in range(len(self.net.listLayer[-2].listNeurons)):
			x = self.dC_dAljk(indexLastLayer,k,finalValues,True)
			finalValues1.append(x)
		finalValues = finalValues1
		self.net = netc
		
		# all Layers
		il = indexLastLayer-1 #index of the layer before the last one 
		for l in range(len(self.net.listLayer)-2):
			# layer l
			for j in range(len(self.net.listLayer[il-l].listNeurons)):
				# New bias
				x =  h*self.dC_dBlj(il-l,j,finalValues[j])
				netc.listLayer[il-l].listNeurons[j].bias = self.net.listLayer[il-l].listNeurons[j].bias - x
				# New Weights 
				for k in range(len(self.net.listLayer[il-l-1].listNeurons)):
					x = h*self.dC_dWljk(il-l,j,k,finalValues[j])
					netc.listLayer[il-l].listW[j][k] = self.net.listLayer[il-l].listW[j][k] - x
			# New finalValues
			finalValues1 = []
			for k in range(len(self.net.listLayer[il-l-1].listNeurons)):
				x = self.dC_dAljk(il-l,k,finalValues)
				finalValues1.append(x)
			finalValues = finalValues1
			self.net = netc



	def backPropagation(self,inputList,outputList):
		print("Net has started learning.")
		for i in range(len(inputList)):
			print("Net is learning...")
			self.train(inputList[i],outputList[i])
		print("Net has finished learning.")
		return self.net


			







red = Net([2,5,2])
#print(red)
print("")
print(red.calculate([0.1,0.03]))

#Data
initial = []
final = []
for i in range(10000):
	initial.append([0.1,(i%10)/100])
	final.append([0.1+(i%10)/100,0])
	

entrenador = Trainer(red)
redEntrenada = entrenador.backPropagation(initial,final)
print("---------------------------------")
#print(redEntrenada)
print("")
print("0.1+0.02 = " + str(redEntrenada.calculate([0.1,0.02])))
print("0.1+0.03 = " + str(redEntrenada.calculate([0.1,0.03])))
print("0.1+0.04 = " + str(redEntrenada.calculate([0.1,0.04])))
print("0.1+0.06 = " + str(redEntrenada.calculate([0.1,0.06])))
print("0.1+0.07 = " + str(redEntrenada.calculate([0.1,0.07])))
print("0.1+0.01 = " + str(redEntrenada.calculate([0.1,0.01])))


