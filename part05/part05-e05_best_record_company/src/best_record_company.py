#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t", encoding="UTF-8")
    groups = df.groupby('Publisher')
    s = groups['WoC'].sum() # the indicator for 'best'
    s = s.sort_values() # sort: bottom = 'best'
    m = df['Publisher'] == s.index[-1] # mask: filter list with best company
    return df[m]

def main():
    df = best_record_company()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df)
    

if __name__ == "__main__":
    main()
