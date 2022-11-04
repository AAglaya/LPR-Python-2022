import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")

fig, axs = plt.subplots(2)
titanic['class'].hist(ax=axs[0])
titanic['age'].hist(ax=axs[1], bins=100)
plt.show()

age = titanic.groupby(['class']).agg({'age': "median"})
age_sex = titanic.groupby(['class', 'sex']).agg({'age': "median"})
print(age_sex)

age_sex_class = titanic.groupby(['class', 'sex']).agg({'age': "median", 'survived': 'mean'})
print(age_sex_class)

age_sex_class_mean = titanic.groupby(['sex']).agg({'survived': "mean"})
print(age_sex_class_mean)

delt = titanic.groupby(['survived']).agg({'age': "std"})
print(delt.loc[1])

surv = titanic.groupby(['age']).agg({'survived': "mean"})
surv.plot()
plt.show()

print(titanic['fare'].sum())