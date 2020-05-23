# Modifying dataframes
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
print(df)

df['Is taxed?'] = 'Yes'
print(df)

df['Margin'] = df.Price - df['Cost to Manufacture']

#New column
df['Lowercase Name'] = df.Name.apply(lower)

#return first and last letter of string
mylambda = lambda str: str[0]+str[-1]

mylambda = lambda x: "Welcome to BattleCity!" if x >= 13 else "You must be over 13"

get_last_name = lambda x: x.split()[-1]
df['last_name'] = df.name.apply(get_last_name)

 #If we use apply without specifying a single column and add the argument axis=1, the input to our lambda function will be an entire row, not a column.
 total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) if row.hours_worked > 40  else row.hourly_wage * row.hours_worked
  
df['total_earned'] = df.apply(total_earned, axis = 1)

print(df)

# Rename columns here
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
print(df)

# Rename columns here
df.rename(columns={
  'name' : 'movie_title'
},
inplace=True)

orders['shoe_source'] = orders.shoe_material.apply(lambda x: \
                        	'animal' if x == 'leather'else 'vegan')

orders['salutation'] = orders.apply(lambda row: \
                                    'Dear Mr. ' + row['last_name']
                                    if row['gender'] == 'male'
                                    else 'Dear Ms. ' + row['last_name'],
                                    axis=1)