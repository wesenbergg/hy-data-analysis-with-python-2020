#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t', encoding='utf-8', index_col='Pos')
    return df.iloc[0:10, 1:3]

def main():
    print(subsetting_by_positions())

if __name__ == "__main__":
    main()
