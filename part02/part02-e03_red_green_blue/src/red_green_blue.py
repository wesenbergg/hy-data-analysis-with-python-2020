#!/usr/bin/env python3

import re

#cwd: hy/hy-data-analysis-with-python-2020/part02-e02_file_listing/
def red_green_blue(filename="src/rgb.txt"):
    lines = []
    with open(filename, "r") as f:
        re.match(r'', filename)
        for line in f:
            line = line.strip()
            line = re.split(r'\s+', line)
            color = line[:3]
            name = line[3:]
            line = "\t".join(color)+"\t"+" ".join(name)
            print(line)
            lines.append(line)
            
    lines.pop(0)
    print(lines[0])
    return lines


def main():
    red_green_blue()

if __name__ == "__main__":
    main()
