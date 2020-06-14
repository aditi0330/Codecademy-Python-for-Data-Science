import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import glob

files = glob.glob("states*.csv")
df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

us_census = pd.concat(df_list)

print(us_census.columns)
print(us_census.dtypes)

split_df = us_census['Income'].str.split('$', expand=True)
us_census.Income = pd.to_numeric(split_df[1])
print(us_census.head())

split_df = us_census['GenderPop'].str.split("_")

us_census['Men'] = split_df.str.get(0)
us_census['Women'] = split_df.str.get(1)

split_df = us_census['Men'].str.split('M', expand=True)
us_census.Men = pd.to_numeric(split_df[0])

split_df = us_census['Women'].str.split('F', expand=True)
us_census.Women = pd.to_numeric(split_df[0])

print(us_census.head())

plt.scatter(us_census.Men, us_census.Women)
plt.show()




