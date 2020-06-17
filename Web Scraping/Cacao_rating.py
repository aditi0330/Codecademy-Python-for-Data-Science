import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html")
soup = BeautifulSoup(webpage.content, "html.parser")

print(soup)

ratings = []
chocolate_ratings = soup.find_all("td", {"class":"Rating"})
for rating in chocolate_ratings[1:]:
    ratings.append(float(rating.get_text()))
    
plt.hist(ratings)

company_tags = soup.select(".Company")
companies_names = []
for company in company_tags[1:]:
    companies_names.append(company.get_text())

cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")
for td in cocoa_percent_tags[1:]:
    percent = float(td.get_text().strip('%'))
    cocoa_percents.append(percent)

d = {"Empresa": companies_names, "Avaliação": ratings, "Porcentagem Cacau": cocoa_percents}
dataframe = pd.DataFrame.from_dict(d)

print(dataframe)

mean_vals = dataframe.groupby("Empresa").mean()

ten_best = mean_vals.nlargest(10, "Avaliação")
print(ten_best)

plt.scatter(dataframe["Porcentagem Cacau"], dataframe.Avaliação)
plt.show()

