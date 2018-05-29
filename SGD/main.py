import mnist_loader
import network
import sys
import time

def main():
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    net = network.Network([784, 30, 10])
    if sys.argv < 2:
        net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
    else:
        net.SGD(training_data, int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), test_data=test_data)

if __name__ == "__main__":
    main()
