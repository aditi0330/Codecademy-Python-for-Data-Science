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

#Modifying error bars
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv("gradebook.csv")

sns.barplot(data=gradebook, x="name", y="grade", ci='sd')
plt.show()

#Calculating different aggregates

df = pd.read_csv("survey.csv")
print(df)
sns.barplot(data=df, x='Gender', y='Response', estimator=len)
plt.show()


df = pd.read_csv("survey.csv")
print(df)
sns.barplot(data=df, x='Gender', y='Response', estimator=np.median)
plt.show()

#Aggregating by multiple columns
df = pd.read_csv("survey.csv")
sns.barplot(data=df, x='Age Range', y='Response', hue='Gender')
plt.show()