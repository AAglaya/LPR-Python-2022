import pandas as pd

df = pd.read_csv("telecom_churn.csv")
states = set(df["State"])

df_new = pd.DataFrame()

for state in states:
    sum_calls = df[df["State"] == state]['Total day calls'].sum()
    state_num = df[df["State"] == state].shape[1]
    df_new.loc[state, 0] = sum_calls/state_num

print(df_new)