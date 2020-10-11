#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    # print(s.index)
    return pd.Series(s.index, index=s.values)

def main():
    s1 = pd.Series(['Alfa', 'Beta', 'Charlie'])
    print(s1)
    s1 = inverse_series(s1)
    print(s1)


if __name__ == "__main__":
    main()
