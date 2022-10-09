import pandas as pd

df = pd.read_csv("telecom_churn.csv")

df_new = df.loc[[100,102,104],['State', 'Churn']]
print(df_new)