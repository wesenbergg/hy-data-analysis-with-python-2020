#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

n = 20 # Number of data points

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)
    # print(model.coef_)
    return model.coef_[0], model.intercept_
    
def main():
    np.random.seed(0)
    x=np.linspace( 0, 10, n )
    y=x*2 + 1 + 1*np.random.randn( n ) # Standard deviation 1

    slope, intercept = fit_line(x, y)
    print(f'Slope: {slope:.2f}\nIntercept: {intercept:.2f}')

    plt.plot(x,y, 'o') # Original datapoints
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, color='red') # Fit-line
    
    plt.show()

    
if __name__ == "__main__":
    main()
