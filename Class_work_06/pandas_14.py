import pandas as pd

df = pd.read_csv("telecom_churn.csv")

df_new = pd.DataFrame({"день": [1, 2, 0], "вечер": [4, 5, 0], "ночь": [0, 0, 0]}, index = ["число минут", "число звонков", 'среднее время звонка'])
df_new.iloc[0, 0] = df["Total day minutes"].mean()
df_new.iloc[1, 0] = df["Total day calls"].mean()
df_new.iloc[2, 0] = df_new.iloc[0, 0]/df_new.iloc[1, 0]
df_new.iloc[0, 1] = df["Total eve minutes"].mean()
df_new.iloc[1, 1] = df["Total eve calls"].mean()
df_new.iloc[2, 1] = df_new.iloc[0, 1]/df_new.iloc[1, 1]
df_new.iloc[0, 2] = df["Total night minutes"].mean()
df_new.iloc[1, 2] = df["Total night calls"].mean()
df_new.iloc[2, 2] = df_new.iloc[0, 2]/df_new.iloc[1, 2]

print(df_new)