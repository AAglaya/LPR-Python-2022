import pandas as pd

df = pd.read_csv("telecom_churn.csv")

df_new = pd.DataFrame(df.groupby("Customer service calls").agg(Emount=("Customer service calls", "count")))

print(df_new)