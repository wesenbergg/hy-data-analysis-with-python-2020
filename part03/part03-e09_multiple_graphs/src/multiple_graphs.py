#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main():
    a_x = np.array([1, 2, 3, 4])
    a_y = np.array([4,2,3,1])
    b_x = np.array([2, 4, 6, 7])
    b_y = np.array([4,3,5,1])
    plt.plot(b_x, b_y, label="line2")      # plot the points in the array a
    plt.plot(a_x, a_y, label="line1")      # plot the points in the array a
    plt.title("Title")              # Add a title to the figure
    plt.xlabel("x-axis")         # Give a label to the x-axis
    plt.ylabel("y-axis")         # Give a label to the y-axis
    plt.show()                      # Tell matplotlib to output the figure.
                                    # Not strictly required in notebooks (but a bit neater).

if __name__ == "__main__":
    main()
