#Quartiles
from song_data import songs
import numpy as np

#Create the variables songs_q1, songs_q2, and songs_q3 here:
#print(songs)
songs_q1 = np.quantile(songs, 0.25)
songs_q2 = np.quantile(songs, 0.50)
songs_q3 = np.quantile(songs, 0.75)
favorite_song = 188.70812
quarter = 2
#Ignore the code below here:
try:
  print("The first quartile of dataset one is " + str(songs_q1) + " seconds")
except NameError:
  print("You haven't defined songs_q1")
try:
  print("The second quartile of dataset one is " + str(songs_q2)+ " seconds")
except NameError:
  print("You haven't defined songs_q2")
try:
  print("The third quartile of dataset one is " + str(songs_q3)+ " seconds")
except NameError:
  print("You haven't defined songs_q3\n")
  
#Quantiles

# Define quartiles, deciles, and tenth here:
quartiles = np.quantile(songs, [0.25, 0.5, 0.75])
deciles = np.quantile(songs, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
tenth  = 3 #170
#Ignore the code below here:
try:
  print("The quartiles are " + str(quartiles) + "\n")
except NameError:
  print("You haven't defined quartiles.\n")
try:
  print("The deciles are " + str(deciles) + "\n")
except NameError:
  print("You haven't defined deciles.\n")

#Interquartile range
#The interquartile range is the difference between the third quartile (Q3) and the first quartile (Q1). 

q1 = np.quantile(songs, 0.25)
#Create the variables q3 and interquartile_range here:
q3 = np.quantile(songs, 0.75)
interquartile_range = q3 - q1
# Ignore the code below here
try:
  print("The first quartile of the dataset is " + str(q1) + "\n")
except NameError:
  print("You haven't defined q1 yet\n")
  
try:
  print("The third quartile of the dataset is " + str(q3) + "\n")
except NameError:
  print("You haven't defined q3 yet\n")
  
try:
  print("The IQR of the dataset is " + str(interquartile_range) + "\n")
except NameError:
  print("You haven't defined interquartile_range yet\n")
  
#Using iqr function
from song_data import songs
from scipy.stats import iqr

#Create the variables interquartile_range here:
interquartile_range = iqr(songs)

# Ignore the code below here
try:
  print("The IQR of the dataset is " + str(interquartile_range) + "\n")
except NameError:
  print("You haven't defined interquartile_range yet\n")
  
#A statistic is robust when outliers have little impact on it.