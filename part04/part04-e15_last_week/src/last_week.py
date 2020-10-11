#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t', encoding='UTF-8' )

    df = df.replace(['Re', 'New'], np.nan) # Col from object to float
    df['LW'] = df['LW'].astype('float64')
    df = df.where(df['LW'].notnull())
    df = df.dropna(axis=0)

    
    df = df.sort_values('LW')
    df.index = df['LW'] # Re indexing to LW col
    df = df.reindex(range(1,41))

    df['WoC'] = df['WoC'] - 1 # Update WoC col

    m1 = (df['Peak Pos'] == df['Pos']) # Update Peak pos col
    m2 = (df.index > df['Pos'])
    df.loc[m1&m2, 'Peak Pos'] = np.nan

    df['Pos'] = range(1,41)
    df['LW'] = np.nan
    return df

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
