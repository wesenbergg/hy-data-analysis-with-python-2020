#!/usr/bin/env python3

import sys

def file_count(filename):
    line_count, word_count, char_count = 0, 0, 0

    with open(filename, 'r') as f:
        for line in f:
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)
    return (line_count, word_count, char_count)

#Count lines, words and characters
def main():
    # arg='test.txt' #kovakoodattu arvo
    for arg in sys.argv[1:]:
        ln, wd, ch = file_count(arg)
        print(f"{ln}\t{wd}\t{ch}\t{arg}")

if __name__ == "__main__":
    main()
