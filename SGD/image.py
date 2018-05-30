from __future__ import print_function
import mnist_loader
import network
import sys


def main():
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    num = sys.argv[1]
    print(num)
    for i in range(28):
        for j in range(28):
            k = (i*28)+j
            temp = int(test_data[int(num)][0][k]*10)
            if temp >= 7:
                print(str(temp) +" ", end='')
            else:
                print(" " +" ", end='')
        i = i+28
        print("\n")
    print(test_data[int(num)][1])

if __name__ == "__main__":
    main()
