import pandas as pd

df = pd.read_csv("telecom_churn.csv")

print(df.groupby("State").agg({"Total day charge": "mean"}).sort_values(by="Total day charge", ascending=True))