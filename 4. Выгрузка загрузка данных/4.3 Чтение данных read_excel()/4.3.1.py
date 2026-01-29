import pandas as pd


df_2017 = pd.read_excel("USD000UTSTOM_170101_171231.xlsx", usecols=["<HIGH>", "<LOW>"])
print((df_2017["<HIGH>"].max() - df_2017["<LOW>"].min()).round(2))

df_2022 = pd.read_excel("USD000UTSTOM_220101_221231.xlsx", usecols=["<HIGH>", "<LOW>"])
print((df_2022["<HIGH>"].max() - df_2022["<LOW>"].min()).round(2))
