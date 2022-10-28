import pandas as pd

df = pd.read_csv("telecom_churn.csv")

print(df.groupby("Churn").agg({"Total day charge" : "mean"}))