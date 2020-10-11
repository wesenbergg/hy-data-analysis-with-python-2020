#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    i_prod = np.sum( (X*Y), axis=1 )
    x_len = scipy.linalg.norm(X, 2, axis=1)
    y_len = scipy.linalg.norm(Y, 2, axis=1)
    a = i_prod / ( x_len*y_len )
    a = np.clip(a, -1, 1)
    return np.arccos(a) / np.pi * 180

def main():
    np.random.seed(0)
    X=np.random.randint(-100, 100, (3,4))
    Y=np.random.randint(-100, 100, (3,4))
    print(vector_angles(X, Y))
    np.array([])

if __name__ == "__main__":
    main()
