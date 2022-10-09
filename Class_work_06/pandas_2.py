import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})
df["C"] = 1
df["D"] = df["A"] + df["B"]
df["E"] = df["D"].apply(lambda x: x ** 2)
df["F"] = df[["A", "C", "E"]].apply(lambda x: x.sum(), axis=1)
print(df)

#В i-ую строку столбеца F записывается записывается сумма элементов df[i][A], df[i][C], df[i][E]
#Например, для 0 строки: 1 + 1 + 36 = 38