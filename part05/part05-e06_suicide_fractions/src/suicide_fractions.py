#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv", sep=",", encoding="UTF-8")
    df['suicide per capita'] = df['suicides_no'] / df['population']
    groups = df.groupby('country')
    return groups['suicide per capita'].mean()

def main():
    s = suicide_fractions()
    print(s.sort_values(ascending=False)[:50])

if __name__ == "__main__":
    main()
