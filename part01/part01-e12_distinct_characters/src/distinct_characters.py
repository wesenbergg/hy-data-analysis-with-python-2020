#!/usr/bin/env python3

def distinct_characters(L):
    tulos = {}
    for e in L:
        tulos[e] = len(set(e))

    return tulos

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
