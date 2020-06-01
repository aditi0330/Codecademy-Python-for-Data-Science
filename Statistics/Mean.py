# Import packages

import numpy as np
import pandas as pd

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save transaction times to a separate numpy array
author_ages = greatest_books['Ages']

# Use plt.hist() below
plt.hist(author_ages, range=(10, 80), bins=14,  edgecolor='black')
plt.title("Age of Top 100 Authors at Publication")
plt.xlabel("Age")
plt.ylabel("Count")

plt.show()

# Use numpy to calculate the average age of the top 100 authors
average_age = np.average(author_ages)

print("The average age of the 100 greatest authors, according to a survey by Le Monde, is: " + str(average_age))