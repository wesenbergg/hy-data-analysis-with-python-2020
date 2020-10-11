#!/usr/bin/env python3
import pandas as pd    # This is the standard way of importing the Pandas library
import numpy as np

def read_series():
    user_input = ""
    arr = np.array([])
    while True:
        user_input = input("Write index and value separeted with whitespace: ")
        if user_input == "": break

        sliced_input = user_input.split()
        if len(sliced_input) == 2:
            arr = np.append(arr, sliced_input)
        else:
            print("Malformed input")
    arr = arr.reshape(len(arr)//2, 2)

    return pd.Series(arr[:, 1], index=arr[:, 0])

def main():
    # wh = pd.read_csv("https://raw.githubusercontent.com/csmastersUH/data_analysis_with_python_2020/master/kumpula-weather-2017.csv")
    # wh.head()   # The head method prints the first 5 rows
    # wh["Snow depth (cm)"].head()     # Using the tab key can help enter long column names
    # wh["Air temperature (degC)"].mean()    # Mean temperature
    print(read_series())
    

if __name__ == "__main__":
    main()
