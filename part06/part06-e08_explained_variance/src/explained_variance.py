#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def stringify_data(d):
    d = [ f'{num:.3f}' for num in d ]
    return ' '.join(d)

def explained_variance():
    X = pd.read_csv('src/data.tsv', sep='\t')
    model = PCA().fit(X)
    return X.var(), model.explained_variance_

def main():
    v, ev = explained_variance()
    print(f'The variances are: {stringify_data(v)}\nThe explained variances after PCA are: {stringify_data(ev)}')
    plt.plot(range(1, len(ev)+1), np.cumsum(ev))
    plt.show()

if __name__ == "__main__":
    main()
