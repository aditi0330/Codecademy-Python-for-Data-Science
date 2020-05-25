
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(10))
ad_clicks.groupby('utm_source')\
    .user_id.count()\
    .reset_index()
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(columns = 'is_click', index = 'utm_source', values = 'user_id').reset_index()

clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])
print(clicks_pivot)
ad_clicks.groupby('experimental_group').user_id.count().reset_index()
ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index().pivot(index = 'experimental_group', columns = 'is_click', values = 'user_id').reset_index()
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_clicks_pivot = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(index='day', columns = 'is_click', values = 'user_id').reset_index()
a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True]/(a_clicks_pivot[True] + a_clicks_pivot[False])
print(a_clicks_pivot)

b_clicks_pivot = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(index='day', columns = 'is_click', values = 'user_id').reset_index()
b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True]/(b_clicks_pivot[True] + b_clicks_pivot[False])
print(b_clicks_pivot)