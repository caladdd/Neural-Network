import mnist_loader
import network
import sys
import time
import image

def main():
    
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    net = network.Network([784, 30, 10])
    if sys.argv < 2:
        net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
    else:
        net.SGD(training_data, 1, 1, float(sys.argv[1]), test_data=test_data)

    while(True):

        a = input("Ingrese una prueba: ")
        #print(len(training_data))
        #print(len(training_data[0][0]))
        print(int(a))
        
        l = net.feedforward(test_data[int(a)][0])
        print("Respuesta dada")
        for i,x in enumerate(l):
            print(i, str(x*100)+"%")
        print("")
        print("Respuesta verdadera")
        print(test_data[int(a)][1])


if __name__ == "__main__":
    main()
