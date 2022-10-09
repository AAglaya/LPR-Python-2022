import pandas as pd

df = pd.read_csv("telecom_churn.csv")
state = 'CO'
print(df[df["State"] == state]['Total day calls'].mean())