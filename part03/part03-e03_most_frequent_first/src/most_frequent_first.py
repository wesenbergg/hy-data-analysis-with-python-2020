#!/usr/bin/env python3
import numpy as np

def most_frequent_first(a, c):
    c_col = a[:, c]
    _, uniq_vals, uniq_count = np.unique(c_col, return_counts=True, return_inverse=True,)
    i = np.argsort( uniq_count[uniq_vals] )
    return a[i][::-1]

def main():
    np.random.seed(0)
    a = np.random.randint(0, 10, (8, 8))
    print(a)
    print(most_frequent_first(a, -1))

if __name__ == "__main__":
    main()
