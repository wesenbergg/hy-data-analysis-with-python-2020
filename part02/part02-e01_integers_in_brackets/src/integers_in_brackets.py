#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    lista = " ".join(re.findall(r'\[[\s\t]*[+-]?\d+\s?\]',s))
    return list(map(int, re.findall(r'[-]?\d+', lista)))

def main():
    print(integers_in_brackets("Incorrect result for string afd [asd] [12 ] [a34] [      -43 ]tt [+12]xxx!"))

if __name__ == "__main__":
    main()
