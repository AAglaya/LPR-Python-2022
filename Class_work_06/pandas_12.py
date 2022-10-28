import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("telecom_churn.csv")
df_new = pd.DataFrame(df.groupby("Customer service calls").agg({"Churn": "mean"}))
print(df_new)

plt.plot([i for i in range(df_new.shape[0])], df_new.iloc[:, 0])
plt.show()