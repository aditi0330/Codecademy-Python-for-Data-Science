
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head(10))
print(cart.head(10))
print(checkout.head(10))
print(purchase.head(10))

visits_cart = pd.merge(visits, cart, how = 'left')
print(visits_cart)

visits_cart_rows = len(visits_cart)
print(visits_cart_rows)

null_cart_times = len(visits_cart[visits_cart.cart_time.isnull()])
print(null_cart_times)

print(float(null_cart_times)/visits_cart_rows)

cart_checkout = pd.merge(cart, checkout, how = 'left')
print(cart_checkout)

cart_checkout_rows = len(cart_checkout) 
null_checkout_times = len(cart_checkout[cart_checkout.checkout_time.isnull()])
print(float(null_checkout_times)/cart_checkout_rows) 

checkout_purchase = pd.merge(checkout, purchase, how = 'left')
checkout_purchase_rows = len(checkout_purchase)
null_purchase_times = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])
print(float(null_purchase_times)/checkout_purchase_rows)

all_data = visits.merge(cart, how = 'left').merge(checkout, how = 'left').merge(purchase, how = 'left')
print(all_data.head())

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

print(all_data.time_to_purchase)

print(all_data.time_to_purchase.mean())