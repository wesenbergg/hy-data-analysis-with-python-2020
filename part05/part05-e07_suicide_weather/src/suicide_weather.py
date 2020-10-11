#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv", sep=",", encoding="UTF-8")
    df['suicide per capita'] = df['suicides_no'] / df['population']
    groups = df.groupby('country')
    return groups['suicide per capita'].mean()

def suicide_weather():
    suicide_df = suicide_fractions()
    weather_df = pd.read_html('src/List_of_countries_by_average_yearly_temperature.html')
    weather_df = weather_df[0]
    # converting from object to float ( replacing 'html minus' sign to - )
    weather_df['Average yearly temperature (1961–1990, degrees Celsius)'] = weather_df['Average yearly temperature (1961–1990, degrees Celsius)'].str.replace("\u2212", "-").astype(float)
    weather_df = weather_df.set_index(weather_df['Country']) # Setting country column as index
    weather_df = weather_df.drop(columns="Country")

    common_df = pd.merge(suicide_df, weather_df, left_index=True, right_index=True) # Merge by index
    return (len(suicide_df), len(weather_df), len(common_df), common_df.corr(method='spearman').iloc[1, 0])

def main():
    sw = suicide_weather()
    print(f'Suicide DataFrame has {sw[0]} rows\nTemperature DataFrame has {sw[1]} rows\nCommon DataFrame has {sw[2]} rows\nSpearman correlation: {sw[3]}')

if __name__ == "__main__":
    main()
