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
  from song_data import songs
import numpy as np

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

# Interquartile range