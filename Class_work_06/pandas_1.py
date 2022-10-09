import pandas as pd

df = pd.read_csv("telecom_churn.csv")
new_df = df.loc[4:9, ["State", "Account length", "Area code", "International plan"]]
print(new_df.iloc[:5])
print(new_df.loc[:5])

#iloc вывел строки с 1 по 5 новой таблицы (нумерация строк изменилась, 4->1... 9->5)
#loc вывел до 5 строки по "старой" нумерации строк, т.е всё до 5 строки. Но так как 1, 2, 3
#строки в новой таблице не существует, он вывел 4 и 5
