#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1, 13)))
 
def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
 
    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]
 
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d
 
def bicycle_timeseries():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = split_date(df)
    
    df["Date"] = pd.to_datetime(d[["Year", "Month", "Day", "Hour"]])
    df["Weekday"] = d["Weekday"]
    df['Weekday'] = df['Weekday'].replace("Mon Tue Wed Thu Fri Sat Sun".split(), [1, 2, 3, 4, 5, 6, 7]).astype(int)
    df = df.drop("Päivämäärä", axis=1)
    df = df.set_index("Weekday")
    return df

def commute():
    df = bicycle_timeseries()
    mask = (df['Date'] >= '2017-08-01') & (df['Date'] < '2017-09-01')
    df = df[mask].drop(columns=['Date'])
    groups = df.groupby('Weekday')
    groups = groups.sum()
    return groups
    
def main():
    df = commute()
    fig, ax = plt.subplots()
    ax.plot(df)
    weekdays="x mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(weekdays)

    plt.show()


if __name__ == "__main__":
    main()
