#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt(np.sum(a**2, axis=1))

def main():
    np.random.seed(0)
    a=np.random.randint(-100, 100, (2,2))
    print(f"original:\n{a}\nnew:")
    print(vector_lengths(a))

if __name__ == "__main__":
    main()
