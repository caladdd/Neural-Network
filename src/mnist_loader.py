import pickle
import gzip
import numpy as np

def load_data():
	f = gzip.open('mnist.pkl.gz','rb')
	training_data, validation_data, test_data = pickle.load(f, encoding='latin1')
	f.close()
	return (training_data, validation_data, test_data)

def vectorized_result(j):
	e = np.zeros((10,1))
	e[j] = 1.0
	return e

def load_data_wrapper():
	tr_d, va_d, te_d = load_data()
	training_inputs = [np.reshape(x,(784,1)) for x in tr_d[0]]
	training_results = [vectorized_result(y) for y in tr_d[1]]
	training_data = [training_inputs, training_results]

	#validation_inputs = [np.reshape(x,(784, 1)) for x in va_d[0]]
	#validation_data = zip(validation_inputs, va_d[1])

	#test_inputs = [np.reshape(x,(784, 1)) for x in te_d[0]]
	#test_data = zip(test_inputs, te_d[1])
	#print(len(training_data[0][0]))
	return training_data#, validation_data, test_data)

def example():
	data = load_data_wrapper()
	for i in range(28):
		for j in range(28):
			k = (i*28)+j
			print(str(int(data[0][700][k]*10)/10)+" ", end="")
		i = i+28
		print("\n")

