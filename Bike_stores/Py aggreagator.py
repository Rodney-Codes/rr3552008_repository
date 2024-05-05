#importing important libraries (all might not be of use)
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#get the current working directory
cwd = os.getcwd()

#import all the relevant csv files
brands = pd.read_csv('C:\\Code\\SQL projects\\Bike store database\\brands.csv')
categories = pd.read_csv('C:\\Code\\SQL projects\\Bike store database\\categories.csv')
customers = pd.read_csv('C:\\Code\\SQL projects\\Bike store database\\customers.csv')
order_items = pd.read_csv('C:\\Code\\SQL projects\\Bike store database\\order_items.csv')
orders = pd.read_csv('C:\\Code\\SQL projects\\Bike store database\\orders.csv')
products = pd.read_csv('C:\\Code\\SQL projects\\Bike store database\\products.csv')
staffs = pd.read_csv('C:\\Code\\SQL projects\\Bike store database\\staffs.csv')
stocks = pd.read_csv('C:\\Code\\SQL projects\\Bike store database\\stocks.csv')
stores = pd.read_csv('C:\\Code\\SQL projects\\Bike store database\\stores.csv')

'''
Joins syntax
df1 = pd.merge(products[['brand_id', 'product_name', 'model_year', 'list_price']], brands[['brand_id', 'brand_name']], how = 'left', left_on = 'brand_id', right_on = 'brand_id')
df2 = products.merge(brands, how = 'inner', on = 'brand_id')
'''

#joins the tables
df1 = pd.merge(products, brands, how = 'inner', on = 'brand_id')

#rename colums for better understanding and QC
df1.columns = df1.columns.map(lambda x: 'product_list_price' if x == 'list_price' else x)

df2 = pd.merge(df1, categories, how = 'inner', on = 'category_id')
df3 = pd.merge(df2, order_items, how = 'inner', on = 'product_id')

df3.columns = df3.columns.map(lambda x: 'order_item_list_price' if x == 'list_price' else x)
df3.columns = df3.columns.map(lambda x: 'order_item_quantity' if x == 'quantity' else x)

df4 = pd.merge(df3, orders, how = 'inner', on = 'order_id')
df5 = pd.merge(df4, customers, how = 'inner', on = 'customer_id')

df5.columns = df5.columns.map(lambda x: 'customer_first_name' if x == 'first_name' else x)
df5.columns = df5.columns.map(lambda x: 'customer_last_name' if x == 'last_name' else x)
df5.columns = df5.columns.map(lambda x: 'customer_phone' if x == 'phone' else x)
df5.columns = df5.columns.map(lambda x: 'customer_email' if x == 'email' else x)
df5.columns = df5.columns.map(lambda x: 'customer_street' if x == 'street' else x)
df5.columns = df5.columns.map(lambda x: 'customer_city' if x == 'city' else x)
df5.columns = df5.columns.map(lambda x: 'customer_state' if x == 'state' else x)
df5.columns = df5.columns.map(lambda x: 'customer_zip_code' if x == 'zip_code' else x)

df6 = pd.merge(df5, stores, how = 'inner', on = 'store_id')

df6.columns = df6.columns.map(lambda x: 'store_phone' if x == 'phone' else x)
df6.columns = df6.columns.map(lambda x: 'store_email' if x == 'email' else x)
df6.columns = df6.columns.map(lambda x: 'store_street' if x == 'street' else x)
df6.columns = df6.columns.map(lambda x: 'store_city' if x == 'city' else x)
df6.columns = df6.columns.map(lambda x: 'store_state' if x == 'state' else x)
df6.columns = df6.columns.map(lambda x: 'store_zip_code' if x == 'zip_code' else x)

df7 = pd.merge(df6, staffs, how = 'inner', on = ['store_id', 'staff_id'])

df7.columns = df7.columns.map(lambda x: 'staff_first_name' if x == 'first_name' else x)
df7.columns = df7.columns.map(lambda x: 'staff_last_name' if x == 'last_name' else x)
df7.columns = df7.columns.map(lambda x: 'staff_phone' if x == 'phone' else x)
df7.columns = df7.columns.map(lambda x: 'staff_email' if x == 'email' else x)

df8 = pd.merge(df7, stocks, how = 'inner', on = ['store_id', 'product_id'])

df8.columns = df8.columns.map(lambda x: 'store_quantity' if x == 'quantity' else x)

#export to a output file
df8.to_excel(r'C:\Code\SQL projects\Bike store database\temp_py_code.xlsx', index=False)

#in case we want output in multiple sheets
'''
with pd.ExcelWriter('csv_s/results.xlsx') as writer:
   same_res.to_excel(writer, sheet_name='same')
   diff_res.to_excel(writer, sheet_name='sheet2')
'''
