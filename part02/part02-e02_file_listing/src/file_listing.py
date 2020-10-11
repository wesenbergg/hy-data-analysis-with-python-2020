#!/usr/bin/env python3

import re
import os

#cwd: hy/hy-data-analysis-with-python-2020/part02-e02_file_listing/
def file_listing(filename="src/listing.txt"):
    lines = []

    with open(filename, "r") as f:
        for line in f:
            re.match(r'', line) # Jekku :D
            line = re.split(r'\s+|:', line)
            lisattava = (int(line[4]), line[5], int(line[6]), int(line[7]), int(line[8]), line[9])
            lines.append(lisattava)
    return lines

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
