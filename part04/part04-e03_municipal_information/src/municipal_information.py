#!/usr/bin/env python3

import pandas as pd

def main():
    f = pd.read_csv('src/municipal.tsv', sep='\t')
    columns = f.columns
    col_count = len(columns)
    row_count = len(f)
    
    print(f'Shape: {row_count},{col_count}\nColumns:')
    for c in columns:
        print(c)


if __name__ == "__main__":
    main()
