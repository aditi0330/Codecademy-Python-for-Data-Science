import numpy as np
from data import dataset

quartile_one = np.quantile(dataset, 0.25) 
quartile_three = np.quantile(dataset, 0.75)
# Define your variables here:
iqr = quartile_three-quartile_one
distance = 1.5 * iqr

#one of the most commonly used methods of drawing the whiskers is to 
#extend them 1.5 times the interquartile range from the first and third quartile.

left_whisker = quartile_one - distance
right_whisker = quartile_three + distance
#Ignore the code below here
try:
  print("The interquartile range of the dataset is " + str(iqr) + ".")
except NameError:
  print("You haven't defined iqr.")
  
try:
  print("Each whisker should be " + str(distance) + " units away from the edges of the box.")
except NameError:
  print("You haven't defined distance.")
  
try:
  print("The left whisker should extend to " + str(left_whisker) + " .")
except NameError:
  print("You haven't defined left_whisker.")
  
try:
  print("The right whisker should extend to " + str(right_whisker) + " .")
except NameError:
  print("You haven't defined right_whisker.")
  
import matplotlib.pyplot as plt
from music_data import two_thousand, two_thousand_one, two_thousand_two
plt.boxplot([two_thousand, two_thousand_one, two_thousand_two], labels = ["2000 Songs", "2001 Songs", "2002 Songs"])
plt.show()

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)


a = np.random.normal(1, 1, 1000)
b = np.random.normal(0, 3, 1000)
c = np.random.normal(2, 1.5, 1000)
d = np.random.normal(-4, 5, 1000)
e = np.random.normal(5, 2, 1000)
plt.boxplot([a,b,c,d,e])
plt.show()
plt.subplot(511)
plt.hist(a)
plt.xlim([-20,20])
plt.subplot(512)
plt.hist(b)
plt.xlim([-20,20])
plt.subplot(513)
plt.hist(c)
plt.xlim([-20,20])
plt.subplot(514)
plt.hist(d)
plt.xlim([-20,20])
plt.subplot(515)
plt.hist(e)
plt.xlim([-20,20])
plt.tight_layout()
plt.show()
