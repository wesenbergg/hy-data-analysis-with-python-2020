#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    return pd.read_csv('src/municipal.tsv', sep='\t', encoding='utf-8', index_col='Region 2018', skiprows=[1], skipfooter=178)
    
def main():
    print(municipalities_of_finland())
    
if __name__ == "__main__":
    main()
