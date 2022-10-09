import pandas as pd

df = pd.read_csv("telecom_churn.csv")
states = set(df["State"])

df_new = df.groupby("State").agg({"Total day calls" : "mean", "Total eve calls" : "mean"})
df_new["day > eve"] = df_new["Total day calls"] > df_new["Total eve calls"]

print(df_new)