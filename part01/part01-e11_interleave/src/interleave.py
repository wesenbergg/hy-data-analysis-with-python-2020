#!/usr/bin/env python3

def interleave(*lists):
    list=[]
    for z in zip(*lists):
        list.extend(z)
    return list

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
