#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv('src/presidents.tsv', sep='\t', encoding='utf-8')

    df = df.replace(['one', 'two', '-'], [1, 2, np.nan]) # Replaces
    df['Start'] = df['Start'].apply(lambda x: x.strip(' Jan'))

    df['Vice-president'] = df['Vice-president'].str.title() # name capitalization

    m = df['President'].str.contains(',') # name formatting
    df.loc[m, 'President'] = df['President'].apply(lambda x: ' '.join(x.split(', ')[::-1]))
    m = df['Vice-president'].str.contains(',')
    df.loc[m, 'Vice-president'] = df['Vice-president'].apply(lambda x: ' '.join(x.split(', ')[::-1]))

    df.Start = df.Start.astype(int) # data-types
    df.Last = df.Last.astype(float)
    df.Seasons = df.Seasons.astype(int)

    return df

def main():
    df = cleaning_data()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)

if __name__ == "__main__":
    main()
