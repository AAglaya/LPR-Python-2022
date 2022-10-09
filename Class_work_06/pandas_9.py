import pandas as pd

df = pd.read_csv("telecom_churn.csv")

num_international_plan_str = df.loc[df['International plan'] == 'Yes', 'International plan'].sum()
num_international_plan = num_international_plan_str.count('Yes')
num_voice_mail_plan_str = df.loc[df['Voice mail plan'] == 'Yes', 'Voice mail plan'].sum()
num_voice_mail_plan = num_voice_mail_plan_str.count('Yes')

print(num_international_plan / df.shape[0])
print(num_voice_mail_plan / df.shape[0])