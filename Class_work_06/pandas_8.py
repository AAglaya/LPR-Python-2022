import pandas as pd

df = pd.read_csv("telecom_churn.csv")
states = set(df["State"])

df_new = pd.DataFrame()

for state in states:
    sum_calls = df[df["State"] == state]['Total day calls'].sum()
    sum_calls_eve = df[df["State"] == state]['Total eve calls'].sum()
    state_num = df[df["State"] == state].shape[1]
    df_new.loc[state, 'mean day'] = sum_calls / state_num
    df_new.loc[state, 'mean eve'] = sum_calls_eve / state_num

df_new['day>eve?'] = df_new['mean eve'] < df_new['mean day']

print(df_new)