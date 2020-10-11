#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    all_municipal = len(df)
    m = (df['Population change from the previous year, %'] > 0)
    growing_municipal = len(df[m])
    return growing_municipal / all_municipal

def main():
    frame = pd.read_csv('src/municipal.tsv', sep='\t', encoding='utf-8', index_col='Region 2018')
    percent = growing_municipalities(frame)
    print(f'Proportion of growing municipalities: {percent:.1f}%')

if __name__ == "__main__":
    main()
