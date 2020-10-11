#!/usr/bin/env python3

import sys
from math import sqrt

def summary(filename):
    sum = 0
    count = 0
    numberList = []
    with open(filename, 'r') as f:
        for line in f:
            try:
                number = float(line.strip())
            except ValueError:
                print("Invalid float")
                continue
            numberList.append(number)
            sum += number
            count += 1
    
    ka = sum/count
    jakaumaSumma = 0
    for i in numberList:
        jakaumaSumma += (i-ka)**2
    jakauma = sqrt( jakaumaSumma * 1/(count-1))

    return (sum, float(ka), float(jakauma))

def main():
    for arg in sys.argv[1:]:
        sm, avg, std = summary(arg)
        print( f"File: {arg} Sum: {sm:.6f} Average: {avg:.6f} Stddev: {std:.6f}" )
    # print(summary("hy/hy-data-analysis-with-python-2020/part02-e05_summary/src/example.txt"))

if __name__ == "__main__":
    main()
