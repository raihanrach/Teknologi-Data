# -*- coding: utf-8 -*-
"""1841720167_8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16G85g500cVxEktOp0SpoXaaGZ8SE_9y7
"""

df = pd.read_excel('/content/drive/MyDrive/OnlineRetail.xlsx')
df.info()
print(df.isnull().any())
print(df.isnull().sum())
print(df[df['Description'].isnull()].head())
print(df[df['CustomerID'].isnull()].head())

dfcleaned = df.dropna(axis=0)

print('df: ' , len(df), ' | ', 'dfcleaned: ', len(dfcleaned))
print('df - dfcleaned = ' , len(df)-len(dfcleaned))

print((dfcleaned['UnitPrice']<=0.0).sum())

print(dfcleaned[dfcleaned['UnitPrice']<=0.0].head())