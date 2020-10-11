#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    R2 = []
    X = df.iloc[:, 0:5]
    Y = df.iloc[:, 5]

    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(X, Y)
    
    R2.append( model.score(X, Y) ) # PART 1

    #PART 2
    for i in range(5):
        x_fit = X.iloc[:, i].values.reshape(-1, 1)
        model.fit(x_fit, Y)
        R2.append( model.score(x_fit, Y) )

    return R2
    
def main():
    print(coefficient_of_determination())

if __name__ == "__main__":
    main()
