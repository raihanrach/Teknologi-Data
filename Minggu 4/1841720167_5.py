# -*- coding: utf-8 -*-
"""1841720167_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16G85g500cVxEktOp0SpoXaaGZ8SE_9y7
"""

import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/fifa.csv')
df.info()

df.set_index('Date', inplace=True)
df.info()

print(df.head())