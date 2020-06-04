import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")
print(data.head())
life_expectancy = data['Life Expectancy']
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.50, 0.75])
gdp = data['GDP']
median_gdp = np.quantile(gdp, 0.5)
print(median_gdp)
plt.hist(life_expectancy)
plt.show()