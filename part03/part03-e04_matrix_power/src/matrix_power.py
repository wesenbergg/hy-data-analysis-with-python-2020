#!/usr/bin/env python3
import numpy as np
from functools import reduce

def func(res, cur):
    print(f"res: {res} cur: {cur}")
    return cur+res

def matrix_power(a, n):
    # if( n == 0 ): return np.eye(a.shape[1], dtype=int) # case when pow = 0
    # if( n == 1 ): return a
    if( n < 0 ): a = np.linalg.inv(a) # case: negative pow
    # mat_pow = a
    # reduce(lambda l, c: l+c ,range(1))
    # for i in range(abs(n)-1):
    #     mat_pow = mat_pow@a
    mat_pow = reduce(np.matmul, (a for _ in range(abs(n)) ), np.eye(a.shape[0]))
    return mat_pow

def main():
    n = -3
    a = np.array([  [1, 2],
                    [3, 4]  ])
    print(np.linalg.matrix_power(a, n))
    print(matrix_power(a, n))

if __name__ == "__main__":
    main()
