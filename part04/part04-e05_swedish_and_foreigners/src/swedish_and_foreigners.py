#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv('src/municipal.tsv', sep='\t', encoding='utf-8', index_col='Region 2018', skiprows=[1], skipfooter=178)
    filter = []
    for e in df['Share of Swedish-speakers of the population, %']:
        filter.append( True if e >= 5.0 else False )
    df = df[filter]

    filter = []
    for e in df['Share of foreign citizens of the population, %']:
        filter.append( True if e >= 5.0 else False )
    df = df[filter]
    return df[['Population', 'Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %']]

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
