import pandas as pd

df = pd.read_csv("telecom_churn.csv")

origin = set(df["Area code"])
print(len(origin))