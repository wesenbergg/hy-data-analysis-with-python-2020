#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    return (pd.Series(L1, index=['a', 'b', 'c']), pd.Series(L2, index=['a', 'b', 'c']))
    
def modify_series(s1, s2):
    s1['d'] = s2['b']
    del s2['b']
    return (s1, s2)
    
def main():
    L1 = ['Alfa', 'Beta', 'Charlie']
    L2 = ['Aapo', 'Bea', 'Carlos']
    s1, s2 = create_series(L1, L2)
    # print(s1 + s2)
    s1, s2 = modify_series(s1, s2)
    print(s1 + s2)
    
if __name__ == "__main__":
    main()
