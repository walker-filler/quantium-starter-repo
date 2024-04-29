import pandas as pd


# Read CSV files
file1 = pd.read_csv('daily_sales_data_0.csv')
file2 = pd.read_csv('daily_sales_data_1.csv')
file3 = pd.read_csv('daily_sales_data_2.csv')

# Filter rows where product is 'Pink Morsels'
file1_pink = file1[file1['product'] == 'Pink Morsels']
file2_pink = file2[file2['product'] == 'Pink Morsels']
file3_pink = file3[file3['product'] == 'Pink Morsels']

# Combine quantity and price into 'sales' field
file1_pink['sales'] = file1_pink['quantity'] * file1_pink['price']
file2_pink['sales'] = file2_pink['quantity'] * file2_pink['price']
file3_pink['sales'] = file3_pink['quantity'] * file3_pink['price']

# Select only the required columns: Sales, Date, Region
file1_final = file1_pink[['sales', 'date', 'region']]
file2_final = file2_pink[['sales', 'date', 'region']]
file3_final = file3_pink[['sales', 'date', 'region']]


result = pd.concat([file1_final, file2_final, file3_final])

result.sort_values(by='date', inplace=True)

result.reset_index(drop=True, inplace=True)

result.to_csv('output.csv', index=False)

