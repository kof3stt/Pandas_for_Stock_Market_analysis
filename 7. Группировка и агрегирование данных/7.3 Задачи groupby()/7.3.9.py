import pandas as pd
import numpy as np


currency_values = [
    ["CNYRUB_TOM", 12.894, 1_000_000, "купля"],
    ["CNYRUB_TOM", 12.905, 2_000_000, "купля"],
    ["USDRUB_TOM", 94.15, 500_000, "продажа"],
    ["EURRUB_TOM", 102.76, 200_000, "купля"],
    ["USDRUB_TOM", 94.15, 500_000, "купля"],
    ["USDRUB_TOM", 94.18, 100_000, "купля"],
    ["CNYRUB_TOM", 12.91, 500_000, "продажа"],
    ["EURRUB_TOM", 102.74, 50_000, "купля"],
    ["USDRUB_TOM", 94.21, 200_000, "купля"],
    ["USDRUB_TOM", 94.215, 20_000, "продажа"],
    ["CNYRUB_TOM", 12.90, 100_000, "купля"],
    ["USDRUB_TOM", 94.24, 300_000, "продажа"],
]
currency_columns = ["Валютная пара", "Цена", "Объем в валюте", "Направление сделки"]
currency = pd.DataFrame(currency_values, columns=currency_columns)
currency["Взвешенная"] = currency["Цена"] * currency["Объем в валюте"]

df = currency.groupby(["Валютная пара", "Направление сделки"]).agg(
    {"Объем в валюте": "sum", "Взвешенная": "sum"}
)
df["Средневзвешенная"] = (df["Взвешенная"] / df["Объем в валюте"]).round(4)
df = df.drop(columns=["Взвешенная", "Объем в валюте"])
print(df)
