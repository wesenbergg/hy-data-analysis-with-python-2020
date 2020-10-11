#!/usr/bin/env python3

import pandas as pd

days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))

def split_date(df):
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
 
    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:,0]
 
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d

def split_date_continues(df1):
    df1 = df1.dropna(how='all', axis=0)
    df1 = df1.dropna(how='all', axis=1)
    df2 = split_date(df1)
    df1 = df1.drop('Päivämäärä', axis=1)

    return pd.concat([df2, df1], axis=1)

def cycling_weather():
    df1 = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df2 = pd.read_csv("src/kumpula-weather-2017.csv", sep=",")

    df1 = df1.dropna(axis=0, how="all")
    df1 = df1.dropna(axis=1, how="all")
    df1 = split_date_continues(df1)

    df = pd.merge(df1, df2, left_on=['Month', 'Day', 'Year'], right_on=['m', 'd', 'Year'])
    df = df.drop(columns=['Time', 'Time zone', 'm', 'd'])
    return df

def main():
    print(cycling_weather())

if __name__ == "__main__":
    main()
