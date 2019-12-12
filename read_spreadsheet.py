#! /usr/bin/env python3

from pandas import DataFrame, read_csv
import pandas as pd

file =  r"~/Downloads/TASK0723990.xlsx"
df = pd.read_excel(file)
systems = df['System']

for i in systems:
    print(i)
