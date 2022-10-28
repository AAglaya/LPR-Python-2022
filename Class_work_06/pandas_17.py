import pandas as pd

df = pd.read_csv("telecom_churn.csv")

x = []
for i in df.columns:
    if not (type(df.loc[0, i]) == str):
        x.append(i)
df_new = df.groupby("Area code").agg({i:"mean" for i in x})

print(df_new)