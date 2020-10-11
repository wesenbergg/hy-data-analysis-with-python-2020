#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv('src/kumpula-weather-2017.csv', sep=',', encoding='utf-8')
    m = (df['Air temperature (degC)'] < 0)
    return len(df[m])

def main():
    print(f'Number of days below zero: {below_zero()}')
    
if __name__ == "__main__":
    main()
