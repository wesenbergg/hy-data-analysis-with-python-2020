#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1, 13)))
weather_df = pd.read_csv('src/kumpula-weather-2017.csv')

def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
 
    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]
 
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d
 
def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = split_date(df)
    df = df.drop("Päivämäärä", axis=1)
    return pd.concat([d, df], axis=1)
 
def cycling_weather():
    wh = pd.read_csv("src/kumpula-weather-2017.csv", encoding='UTF-8')
    bike = split_date_continues()
    result = pd.merge(wh, bike, left_on=["Year", "m", "d"], right_on=["Year", "Month", "Day"])
    return result.drop(['m', 'd', 'Time', 'Time zone'], axis=1)

def cycling_weather_continues(station):
    df = cycling_weather()
    model = LinearRegression(fit_intercept=True)

    daily_sum = df.groupby(['Month', 'Day'])
    daily_sum = daily_sum[station].sum()
    df = pd.merge(weather_df, daily_sum, right_on=['Day', 'Month'], left_on=['d', 'm'])
    df = df.fillna(method='ffill')

    X = df.loc[:, ['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    Y = df.loc[:, station]
    model.fit(X, Y)
    return model.coef_, model.score(X, Y)
    
def main():
    station = 'Eteläesplanadi'
    coef, score = cycling_weather_continues(station)
    print(f'Measuring station:{station}\nRegression coefficient for variable \'precipitation\': {coef[0]:.1f}\nRegression coefficient for variable \'snow depth\': {coef[0]:.1f}\nRegression coefficient for variable \'temperature\': {coef[0]:.1f}\nScore: {score:.2f}')

if __name__ == "__main__":
    main()
