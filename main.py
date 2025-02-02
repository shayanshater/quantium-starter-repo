import numpy as np
import pandas as pd

df0 = pd.read_csv('data/daily_sales_data_0.csv')
df1 = pd.read_csv('data/daily_sales_data_1.csv')
df2 = pd.read_csv('data/daily_sales_data_2.csv')
df = pd.concat([df0,df1,df2], ignore_index=True)



df = df[df['product'] == 'pink morsel']


df['price'] = df['price'].str.replace('$','',regex=False).astype(float)
df['quantity'] = df['quantity'].astype(int)
df['sales'] = df['price'] * df['quantity']


df = df[['sales','date','region']]

df.to_csv('data/formattedData.csv')


