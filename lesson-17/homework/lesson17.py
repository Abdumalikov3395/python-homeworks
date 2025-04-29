import pandas as pd
import numpy as np

#ex1
# data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
# df = pd.DataFrame(data)
# df.rename(columns={'First Name':'first name', 'Age':'age'}, inplace=True)
# print(df.head(3) )
# print(df['age'].mean() )
# print(df[['first name', 'City']])
# df['Salary']=np.random.randint(10000,100000,size=len(df))
# print(df)
# print(df.describe() )

#ex2

# sales_and_expenses=pd.DataFrame()
# sales_and_expenses['Month']=['Jan','Feb','Mar','Apr']
# sales_and_expenses['Sales']=[5000,6000,7500,8000]
# sales_and_expenses['Expenses']=[3000,3500,4000,4500]
# print(sales_and_expenses)
# print(f"Max of Sales {sales_and_expenses['Sales'].max()}, Max of Expenses {sales_and_expenses['Expenses'].max()}")
# print(f"Min of Sales {sales_and_expenses['Sales'].min()}, Min of Expenses {sales_and_expenses['Expenses'].min()}")
# print(f"Avarage of Sales {sales_and_expenses['Sales'].mean()}, Avarage of Expenses {sales_and_expenses['Expenses'].mean()}")

#ex3
# expenses=pd.DataFrame()
# expenses['Category']=['Rent','Utilities','Groceries','Entertainment']
# expenses['January']=[1200,200,300,150]
# expenses['February']=[1300,220,320,160]
# expenses['March']=[1400,240,330,170]
# expenses['April']=[1500,250,350,180]
# print(expenses)
# expenses=expenses.set_index('Category')
# expenses['max expences']=expenses.max(axis=1)
# print(expenses[['max expences']])
# expenses['min expences']=expenses.min(axis=1)
# print(expenses[['min expences']])
# expenses['mean expences']=expenses.mean(axis=1)
# print(expenses[['mean expences']])

