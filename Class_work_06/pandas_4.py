import pandas as pd

df = pd.read_csv("telecom_churn.csv")
state = 'CO'
sum_calls = df[df["State"] == state]['Total day calls'].sum()
state_num = df[df["State"] == state].shape[1]
print(sum_calls/state_num)