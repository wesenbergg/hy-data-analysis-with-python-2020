#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv('src/kumpula-weather-2017.csv', sep=',', encoding='utf-8')
    m = (df['m'] == 7)
    df = df[m]
    return df['Air temperature (degC)'].mean()

def main():
    print(f'Average temperature in July: {average_temperature():.1f}')

if __name__ == "__main__":
    main()
