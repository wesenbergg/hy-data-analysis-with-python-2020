#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv('src/kumpula-weather-2017.csv', sep=',', encoding='utf-8') #index_col='Pos'
    df = df['Snow depth (cm)']
    return df.max()

def main():
    print(f'Max snow depth: {snow_depth():.1f}')

if __name__ == "__main__":
    main()
