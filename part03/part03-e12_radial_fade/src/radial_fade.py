#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    center_y = a.shape[0]
    center_x = a.shape[1]
    # print(f'{w/2}, {h/2}')
    return (center_y/2-0.5, center_x/2-0.5)   # note the order: (center_y, center_x)

def radial_distance(a):
    arr = np.zeros((a.shape[0], a.shape[1]))
    c = center(a)
    for i, v in np.ndenumerate(arr):
        arr[i] = np.linalg.norm(np.array(i)-np.array(c))
    return np.array(arr)

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    return np.interp(a, (a.min(), a.max()), (tmin, tmax))

def radial_mask(a):
    return scale(1 - radial_distance(a))

def radial_fade(a):
    return a * radial_mask(a).reshape(a.shape[0], a.shape[1], 1)

def main():
    image = plt.imread('src/painting.png')
    # print(center(image))
    # print(radial_distance(image))
    # plt.imshow(scale(image, 0.3, 0.6))
    # print(scale(image))
    # plt.imshow(radial_fade(image))

    plt.subplot(3, 1, 1)
    plt.imshow(radial_mask(image))
    plt.subplot(3, 1, 2)
    plt.imshow(scale(image, 0.3, 0.6))
    plt.subplot(3, 1, 3)
    plt.imshow(radial_fade(image))

    plt.show()

if __name__ == "__main__":
    main()
