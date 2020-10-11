#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    diskriminantti=b**2-4*a*c
    print(diskriminantti)
    if diskriminantti == 0:
        tulos=-b/(2*a)
        return (tulos, tulos)
    elif diskriminantti > 0:
        sqr=math.sqrt(diskriminantti)
        tulos1=(-b+sqr)/(2*a)
        tulos2=(-b-sqr)/(2*a)
        return (tulos1, tulos2)
    elif diskriminantti < 0:
        print("ei nollakohtia")

    return (0,0)


def main():
    print(solve_quadratic(1,-3,2))

if __name__ == "__main__":
    main()
