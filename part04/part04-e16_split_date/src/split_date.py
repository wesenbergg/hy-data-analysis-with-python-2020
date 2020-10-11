#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';', encoding='utf-8')
    df = df.dropna(how='all', axis=0)
    df = df.dropna(how='all', axis=1)
    df = pd.DataFrame(df['Päivämäärä'].str.split(' ', 4).tolist(), columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour'])
    df = df.replace(['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su'], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    df = df.replace(['tammi', 'helmi', 'maalis', 'huhti', 'touko', 'kesä', 'heinä', 'elo', 'syys', 'loka', 'marras', 'joulu'], range(1,13))
    df['Day'] = df['Day'].astype('int32')
    df['Year'] = df['Year'].astype('int32')
    df['Hour'] = df['Hour'].apply(lambda x: x.strip('0'))
    df['Hour'] = df['Hour'].apply(lambda x: x.strip(':'))
    df['Hour'] = df['Hour'].replace('', '0')
    df['Hour'] = df['Hour'].astype('int32')
    return df

def main():
    df = split_date()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)
       
if __name__ == "__main__":
    main()
