import pandas as pd

df = pd.read_csv("telecom_churn.csv")
df_new = pd.DataFrame()

df['Total calls'] = df[["Total day calls", "Total eve calls"]].apply(lambda x: x.sum(), axis=1)
df_new = df.groupby(["Total calls"]).agg({"Total calls": "count"})

print(df_new)