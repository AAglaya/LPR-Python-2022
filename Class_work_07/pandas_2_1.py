import pandas as pd
import numpy as np

df = pd.DataFrame({
'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
'purch_amt': [150.5, np.nan, 65.26, 110.5, 948.5, np.nan, 5760, 1983.43, np.nan, 250.45, 75.29, 3045.6],
'sale_amt': [10.5, 20.65, np.nan, 11.5, 98.5, np.nan, 57, 19.43, np.nan, 25.45, 75.29, 35.6],
'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],
'salesman_id': [5002, 5003, 5001,np.nan, 5002, 5001, 5001,np.nan, 5003, 5002, 5003,np.nan]})


#Индексы пропущенных хначений
for name in ['ord_no', 'purch_amt', 'sale_amt',  'ord_date', 'customer_id', 'salesman_id']:
    mask = pd.isna(df[name])
    print(*list(df[mask][name].index))

#Замена на число
df['ord_no'].fillna(70003, inplace=True)
#Среднее
df['purch_amt'].fillna(df['purch_amt'].mean(), inplace=True)
#Среднее медианное
df['sale_amt'].fillna(df['sale_amt'].median(), inplace=True)
#Замена на самый часто встречающийся
df['ord_date'].fillna(df['ord_date'].value_counts().index[0], inplace=True)
#Интерполяция
df['salesman_id'] = df['salesman_id'].interpolate(method='linear')


print(df)