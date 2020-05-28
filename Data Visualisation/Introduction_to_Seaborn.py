#Plotting bars with seaborn
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
df = pd.read_csv('results.csv')
# Load results.csv here:
print(df)

sns.barplot(data=df, x= 'Gender', y= 'Mean Satisfaction')
plt.show()

#Understanding Aggregates
import numpy as np

gradebook = pd.read_csv("gradebook.csv")
print(gradebook)
assignment1 = gradebook[gradebook.assignment_name == 'Assignment 1']
print(assignment1)
asn1_median = np.median(assignment1.grade)
print(asn1_median)

#Plotting Aggregates
gradebook = pd.read_csv("gradebook.csv")
print(gradebook)
sns.barplot(data=gradebook, x='assignment_name', y='grade')
plt.show()