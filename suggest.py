#!/usr/bin/env python
# coding: utf-8

import pandas as pd

df = pd.read_csv("Pricing Calculator (2).csv")

# inp = "p3.2xlarge"
# prov = "AWS"

inp = input("Enter Instance Name : ")
prov = input("Enter Provider : ")

gput = str(df['GPU Type'].values[df['Instance Name']==inp][0])
gpum = df['GPU memory'].values[df['Instance Name']==inp][0]


df2 = df[(df['GPU Type'] == gput) & (df['GPU memory'] == gpum)]
print("\n" + df2.to_string(index=False))


print("\n \n ----------- Minimum Priced instance ------------ \n")
print(df2[df2['Price'] == df2['Price'].min()].to_string(index = False) + "\n")

