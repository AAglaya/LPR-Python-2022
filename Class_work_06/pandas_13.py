import pandas as pd

df = pd.read_csv("telecom_churn.csv")

print(df['Total intl minutes'].sum()/df.shape[0])