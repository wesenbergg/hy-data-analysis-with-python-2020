#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    loaded_data = load()
    sepal_length = loaded_data[:, 0]
    petal_length = loaded_data[:, 2]
    return scipy.stats.pearsonr(sepal_length, petal_length)[0]

def correlations():
    loaded_data = load()
    return np.corrcoef(loaded_data, rowvar=False)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
