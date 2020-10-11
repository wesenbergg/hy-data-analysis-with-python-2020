#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# part 1
def to_grayscale(img):
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    g_img = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return g_img

# part 2
def to_red(img):
    return img * [1, 0, 0]

def to_green(img):
    return img * [0, 1, 0]

def to_blue(img):
    return img * [0, 0, 1]

def main():
    image = plt.imread('src/painting.png')
    
    # part 2
    plt.subplot(3, 1, 1)
    plt.imshow(to_red(image))
    plt.subplot(3, 1, 2)
    plt.imshow(to_green(image))
    plt.subplot(3, 1, 3)
    plt.imshow(to_blue(image))
    plt.show()
    
    # part 1
    plt.gray()
    plt.imshow(to_grayscale(image))
    plt.show()

if __name__ == "__main__":
    main()
