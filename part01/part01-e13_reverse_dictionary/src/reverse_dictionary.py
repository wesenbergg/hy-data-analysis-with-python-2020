#!/usr/bin/env python3

def reverse_dictionary(d):
    tulos = {}
    for k, v in d.items():
        for e in v:
            if e in tulos:
                tulos[e].append(k)
            else:
                tulos[e] = [k]
    return tulos

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
