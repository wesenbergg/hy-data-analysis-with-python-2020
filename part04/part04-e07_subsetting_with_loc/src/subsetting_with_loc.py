#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    df = pd.read_csv('src/municipal.tsv', sep='\t', encoding='utf-8', index_col='Region 2018')
    df = df.loc['Akaa':'Äänekoski', ['Population', 'Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %']]
    return df

def main():
    print(subsetting_with_loc())

if __name__ == "__main__":
    main()
