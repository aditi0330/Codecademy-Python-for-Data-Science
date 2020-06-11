import codecademylib
import pandas as pd

df = pd.read_csv('clicks.csv')

df['is_purchase'] = df.click_day.apply(
  lambda x: 'Purchase' if pd.notnull(x) else 'No Purchase'
)

purchase_counts = df.groupby(['group', 'is_purchase'])\
	.user_id.count().reset_index()

print purchase_counts