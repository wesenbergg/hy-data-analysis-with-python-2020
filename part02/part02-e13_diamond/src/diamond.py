#!/usr/bin/env python3

import numpy as np

def diamond(n):
    q1 = np.fliplr(np.eye(n, dtype=int)) #Starting point: Top-left (quarter).
    q2 = np.eye(n, n-1, -1, int) # Moving clockwise
    q3 = np.eye(n-1, n, 1, int)
    q4 = np.fliplr(np.eye(n-1, k=1, dtype=int))
    right = np.concatenate((q1, q3))
    left = np.concatenate((q2, q4))

    return np.concatenate((right, left), axis=1)

def main():
    print(diamond(5))

if __name__ == "__main__":
    main()