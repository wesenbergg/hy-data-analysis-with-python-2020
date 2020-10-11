#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    mult = np.arange(0, n)
    return mult * mult[:, None]

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
