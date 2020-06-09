#1 Sample T-Testing
# If we receive a p-value of less than 0.05,
# we can reject the null hypothesis and state that there is a significant difference.
from scipy.stats import ttest_1samp
import numpy as np

ages = np.genfromtxt("ages.csv")
print(ages)
ages_mean = np.mean(ages)
tstat, pval = ttest_1samp(ages, 30)
print(pval)

#One Sample T-Test II

correct_results = 0 # Start the counter at 0

daily_visitors = np.genfromtxt("daily_visitors.csv", delimiter=",")

for i in range(1000): # 1000 experiments
   #your ttest here:
   tstatistic, pval = ttest_1samp(daily_visitors[i], 30)
   if pval < 0.05:
     correct_results += 1
   #print the pvalue here:
   print(pval) 
  
print "We correctly recognized that the distribution was different in " + str(correct_results) + " out of 1000 experiments."
print "We correctly recognized that the distribution was different in " + str(correct_results) + " out of 1000 experiments."

#2 Sample T-Test
from scipy.stats import ttest_ind
import numpy as np

week1 = np.genfromtxt("week1.csv",  delimiter=",")
week2 = np.genfromtxt("week2.csv",  delimiter=",")
week1_mean = np.mean(week1)
week2_mean = np.mean(week2)
week1_std = np.std(week1)
week2_std = np.std(week2)
tstatstic, pval = ttest_ind(week1, week2)

#The error probability only gets bigger with the more t-tests we do.

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")
a_mean = np.mean(a)
b_mean = np.mean(b)
c_mean = np.mean(c)
a_std = np.std(a)
b_std = np.std(b)
c_std = np.std(c)
a_test, a_b_pval = ttest_ind(a, b) 
b_test, a_c_pval = ttest_ind(c, a) 
c_test, b_c_pval = ttest_ind(b, c) 
error_prob = 1 - 0.95**3

#ANOVA

from scipy.stats import f_oneway

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b_new.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")
fstat, pval = f_oneway(a, b, c)
print(pval)

#Assumptions of Numerical Hypothesis Tests

import matplotlib.pyplot as plt

dist_1 = np.genfromtxt("1.csv",  delimiter=",")
dist_2 = np.genfromtxt("2.csv",  delimiter=",")
dist_3 = np.genfromtxt("3.csv",  delimiter=",")
dist_4 = np.genfromtxt("4.csv",  delimiter=",")

#plot your histogram here
plt.hist(dist_1)
plt.show()
plt.hist(dist_2)
plt.show()
plt.hist(dist_3)
plt.show()
plt.hist(dist_4)
plt.show()
not_normal = 4
ratio = np.std(dist_2)/np.std(dist_3)

#Tukey's Range Test
