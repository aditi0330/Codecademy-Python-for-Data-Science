#There’s no better tool to visualize the uncertainty and chaos in data than a histogram.
# A histogram displays the distribution of your underlying data.

#Summarising your data
# Import packages
import numpy as np
import pandas as pd

# Read in transactions data
transactions = pd.read_csv("transactions.csv")
transactions = transactions.drop(["Unnamed: 0"], axis = 1)

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values

# Print transactions below
print(transactions)

# Print the average times below
print(np.average(times))

#Range

# Find the minimum time, maximum time, and range
min_time = np.amin(times) 
max_time = np.amax(times)
range_time = max_time - min_time
 
# Printing the values
print("Earliest Time: " + str(min_time))
print("Latest Time: " + str(max_time))
print("Time Range: " + str(range_time))

#Bins and Count
# Import packages

# Array of days old bread
days_old_bread = np.array([0, 8, 7, 8, 0, 2, 3, 5, 6, 2])

# Set the minimum and maximums of the array below
min_days_old = np.amin(days_old_bread)
max_days_old = np.amax(days_old_bread)
# Set the number of bins to 3
bins = 3


# Calculate the bin range
try:
	bin_range = (max_days_old - min_days_old + 1) / bins
	print("Bins: " + str(bins))
	print("Bin Width: " + str(bin_range))
# Printing the values
except:
	print("You have not set the min, max, or bins values yet.")
    
    
#A count is the number of values that fall within a bin’s range.
#A bin is a sub-range of values that falls within the range of a dataset. 

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values

# Use numpy.histogram() below
times_hist = np.histogram(times, range = (0, 24), bins = 4)

print(times_hist)

from matplotlib import pyplot as plt


# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values

plt.hist(times, range = (0, 24), bins = 6) 
plt.show()