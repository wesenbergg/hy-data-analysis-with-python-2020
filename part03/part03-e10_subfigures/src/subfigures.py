#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    print(a[:,0])
    plt.subplot(1, 2, 1)
    plt.plot(a[:,0], a[:,1])
    plt.subplot(1, 2, 2)
    plt.scatter(a[:,0], a[:,1], s=a[:,3], c=a[:,2])
    plt.show()

def main():
    a = np.array([[1,1, 20, 15], [2,4, 20, 15], [3,3, 20, 15], [4,4, 20, 15], [5,5, 20, 15], [6,6, 20, 15]])
    subfigures(a)

if __name__ == "__main__":
    main()
