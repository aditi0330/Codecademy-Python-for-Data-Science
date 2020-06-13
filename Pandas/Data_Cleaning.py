import codecademylib3_seaborn
import pandas as pd

df1 = pd.read_csv("df1.csv")
df2 = pd.read_csv("df2.csv")
print(df1.head())
print(df2.head())
print(df1.info())
print(df2.info())
print(df1.describe())
print(df2.describe())
print(df1.columns)
print(df2.columns)
print(df2['Number'].value_counts())

clean = 2

#We can combine the use of glob, a Python library for working with files, with pandas to organize this data better.
# glob can open multiple files by using regex matching to get the filenames:

import glob
student_files = glob.glob("exam*.csv")
df_list = []
for filename in student_files:
  data = pd.read_csv(filename)
  df_list.append(data)

students = pd.concat(df_list)

print(students)
print(len(students))

# We can use pd.melt() to do this transformation. .melt() takes in a DataFrame, and the columns to unpack:

#frame: the DataFrame you want to melt
#id_vars: the column(s) of the old DataFrame to preserve
#value_vars: the column(s) of the old DataFrame that you want to turn into variables
#value_name: what to call the column of the new DataFrame that stores the values
#var_name: what to call the column of the new DataFrame that stores the variables

from students import students

print(students.columns)
students = pd.melt(frame=students, id_vars=['full_name','gender_age','grade'], value_vars=['fractions', 'probability'], value_name='score', var_name='exam')

print(students.head())
print(students.columns)
print(students.exam.value_counts())


duplicates = students.duplicated()
print(duplicates.head())
print(duplicates.value_counts())
students = students.drop_duplicates()
duplicates = students.duplicated()
print(duplicates.head())
print(duplicates.value_counts())

print(students)
print(students.columns)
print(students.gender_age.head())
students['gender'] = students.gender_age.str[0]
students['age'] = students.gender_age.str[1:]
print(students.head())
print(students[['full_name', 'grade', 'exam', 'score', 'gender', 'age']])
