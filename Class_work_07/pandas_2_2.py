import pandas as pd
from matplotlib import pyplot as plt

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print(diamonds)

#Найдите все алмазы которые по любому линейному размеру больше 5
##print(diamonds[((diamonds["x"] > 5) & (diamonds["y"] > 5) & (diamonds["z"] > 5))])

df = diamonds.select_dtypes(include=['number', 'float'])
##print(df)


##for col in df:
##    print(df[col].mean())


##df_new = diamonds.groupby(["cut"]).agg({"price": "mean"})
##df_new.plot()
##plt.show()


##plt.hist(df['carat'], "auto")
##plt.show()


num = 0
for name in ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y', 'z']:
    mask = pd.isna(diamonds[name])
    print(diamonds[mask][name])
    #if diamonds[mask][name].values == False:
     #   num += 1
print(num)


#df_new2 = diamonds
#for name in ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y', 'z']:
#    df_new2[(pd.isna(diamonds[name]) == False)].pop(name)
#print(df_new2)


