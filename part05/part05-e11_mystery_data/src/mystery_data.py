#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    model = LinearRegression(fit_intercept=False)
    model.fit(df.iloc[:, 0:5], df.iloc[:, 5])
    return model.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here
    print(f'Coefficient of X1 is {coefficients[0]}\nCoefficient of X2 is {coefficients[1]}\nCoefficient of X3 is {coefficients[2]}\nCoefficient of X4 is {coefficients[3]}\nCoefficient of X5 is {coefficients[4]}\n')
    
if __name__ == "__main__":
    main()
