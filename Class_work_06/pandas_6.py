import pandas as pd

df = pd.read_csv("telecom_churn.csv")

df = df[df["Total day calls"] > df["Total day calls"].mean()]
print(df)