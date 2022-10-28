import pandas as pd

df = pd.read_csv("telecom_churn.csv")

print(((df["International plan"] == "Yes") & (df["Voice mail plan"])).mean())