import pandas as pd
import numpy as np
import sqlite3

# ===============================
# Homework Assignment 1: Sales Data
# ===============================
sales_df = pd.read_csv('task/sales_data.csv')

# 1. Group by Category
category_stats = sales_df.groupby('Category').agg(
    total_quantity_sold=('Quantity', 'sum'),
    average_price=('Price', 'mean'),
    max_quantity_single_transaction=('Quantity', 'max')
).reset_index()

# 2. Top-selling product in each category
top_products = (
    sales_df.groupby(['Category', 'Product'])['Quantity']
    .sum()
    .reset_index()
    .sort_values(['Category', 'Quantity'], ascending=[True, False])
    .drop_duplicates('Category')
)

# 3. Date with highest total sales (Quantity * Price)
sales_df['TotalSales'] = sales_df['Quantity'] * sales_df['Price']
top_sales_date = (
    sales_df.groupby('Date')['TotalSales']
    .sum()
    .reset_index()
    .sort_values('TotalSales', ascending=False)
    .iloc[0]
)

# ===============================
# Homework Assignment 2: Customer Orders
# ===============================
orders_df = pd.read_csv('task/customer_orders.csv')

# 1. Customers with 20+ orders
order_counts = orders_df.groupby('CustomerID')['OrderID'].nunique().reset_index()
order_counts_20plus = order_counts[order_counts['OrderID'] >= 20]

# 2. Customers with avg price per unit > 120
avg_price_customers = orders_df.groupby('CustomerID')['Price'].mean().reset_index()
high_price_customers = avg_price_customers[avg_price_customers['Price'] > 120]

# 3. Total quantity and total price per product, filter quantity >= 5
product_stats = orders_df.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', lambda x: (x * orders_df.loc[x.index, 'Quantity']).sum())
).reset_index()
filtered_products = product_stats[product_stats['total_quantity'] >= 5]

# ===============================
# Homework Assignment 3: Population Salary Analysis
# ===============================
# Read salary bands from Excel
salary_bands = pd.read_excel('task/population salary analysis.xlsx')

# Read population data from SQLite
conn = sqlite3.connect('task/population.db')
population_df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

# Assume 'Salary' and 'State' columns exist in population table
# Apply salary bands
def assign_salary_band(salary):
    for _, row in salary_bands.iterrows():
        if row['MinSalary'] <= salary <= row['MaxSalary']:
            return row['SalaryBand']
    return 'Unknown'

population_df['SalaryBand'] = population_df['Salary'].apply(assign_salary_band)

# Measures for each salary band
band_group = population_df.groupby('SalaryBand')
salary_band_stats = band_group['Salary'].agg(
    population_size='count',
    average_salary='mean',
    median_salary='median'
).reset_index()
total_population = population_df.shape[0]
salary_band_stats['percentage_population'] = (salary_band_stats['population_size'] / total_population * 100).round(2)

# Measures for each salary band in each state
state_band_group = population_df.groupby(['State', 'SalaryBand'])
state_salary_stats = state_band_group['Salary'].agg(
    population_size='count',
    average_salary='mean',
    median_salary='median'
).reset_index()
state_totals = population_df.groupby('State')['Salary'].count().reset_index(name='state_total')
state_salary_stats = state_salary_stats.merge(state_totals, on='State')
state_salary_stats['percentage_population'] = (state_salary_stats['population_size'] / state_salary_stats['state_total'] * 100).round(2)
state_salary_stats.drop('state_total', axis=1, inplace=True)

# ===============================
# Output Results (you can print or export them as needed)
# ===============================
print("\n--- Sales Category Stats ---\n", category_stats)
print("\n--- Top Selling Product in Each Category ---\n", top_products)
print("\n--- Date with Highest Sales ---\n", top_sales_date)

print("\n--- Customers with >= 20 Orders ---\n", order_counts_20plus)
print("\n--- Customers with Avg Price > $120 ---\n", high_price_customers)
print("\n--- Filtered Products (Quantity >= 5) ---\n", filtered_products)

print("\n--- Salary Band Stats ---\n", salary_band_stats)
print("\n--- State-wise Salary Band Stats ---\n", state_salary_stats)
