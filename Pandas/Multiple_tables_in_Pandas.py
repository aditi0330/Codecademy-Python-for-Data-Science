#Dealing with multiple tables in Pandas
#Creating a DataFrame made by matching the common columns of two DataFrames is called a merge
#We can specify which columns should be matches by using the keyword arguments left_on and right_on
#We can combine DataFrames whose rows don’t all match using left, right, and outer merges and the how keyword argument
#We can stack or concatenate DataFrames with the same columns using pd.concat
import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

#INNER MERGE
sales_vs_targets = pd.merge(sales, targets)
print(sales_vs_targets)
crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]

#Merge three tables
men_women = pd.read_csv('men_women_sales.csv')
all_data = sales.merge(targets).merge(men_women)
print(all_data)
results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]

#Merge using Rename
orders_products = pd.merge(orders, products.rename(columns={'id': 'product_id'}))
print(orders_products)

#left_on and right_on
orders_products = pd.merge(orders, products, left_on='product_id', right_on='id', suffixes=['_orders', '_products'])
print(orders_products)

#OUTER MERGE
store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)
store_a_b_outer = pd.merge(store_a, store_b, how='outer')
print(store_a_b_outer)

store_a_b_left = pd.merge(store_a, store_b, how = 'left')
store_b_a_left = pd.merge(store_b, store_a, how = 'left')
print(store_a_b_left)
print(store_b_a_left)

#Concatenation of dataframes
bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)
menu = pd.concat([bakery, ice_cream])
print(menu)

visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])
print(visits)
print(checkouts)
v_to_c = pd.merge(visits, checkouts)
v_to_c['time'] = v_to_c.checkout_time - \
                 v_to_c.visit_time

print(v_to_c)
print(v_to_c.time.mean())