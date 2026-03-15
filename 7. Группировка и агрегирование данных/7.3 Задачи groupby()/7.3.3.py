import pandas as pd
import numpy as np


depo_values = [
    ["New Energy Bank", 1_000_000_000, 8.30, "O/N"],
    ["AgroFoodBank", 5_000_000_000, 8.50, "1W"],
    ["First Ecologic Bank", 4_500_000_000, 8.60, "1M"],
    ["Golden Silver Bank", 3_800_000_000, 8.67, "1M"],
    ["Big Business Bank", 1_500_000_000, 8.27, "O/N"],
    ["Big Business Bank", 3_000_000_000, 8.30, "O/N"],
    ["New Energy Bank", 6_000_000_000, 8.84, "3M"],
    ["New Energy Bank", 2_000_000_000, 8.32, "O/N"],
    ["First Ecologic Bank", 3_000_000_000, 8.41, "O/N"],
    ["AgroFoodBank", 2_000_000_000, 8.45, "1W"],
    ["AgroFoodBank", 1_000_000_000, 8.30, "O/N"],
    ["Big Business Bank", 2_500_000_000, 8.30, "O/N"],
    ["Golden Silver Bank", 2_500_000_000, 8.65, "1M"],
    ["New Energy Bank", 2_000_000_000, 8.45, "1W"],
    ["First Ecologic Bank", 2_000_000_000, 8.50, "1M"],
    ["Golden Silver Bank", 4_300_000_000, 8.40, "O/N"],
    ["Golden Silver Bank", 2_000_000_000, 8.35, "O/N"],
    ["First Ecologic Bank", 4_000_000_000, 8.55, "1M"],
    ["New Energy Bank", 4_000_000_000, 8.80, "3M"],
]
depo_columns = ["Банк", "Сумма, руб.", "Ставка", "Срок"]
depo = pd.DataFrame(depo_values, columns=depo_columns)
depo["Взвешенная ставка"] = depo["Сумма, руб."] * depo["Ставка"]
df = depo.groupby(["Банк", "Срок"]).agg(
    {"Сумма, руб.": "sum", "Взвешенная ставка": "sum"}
)
df["Средневзвешенная ставка"] = (df["Взвешенная ставка"] / df["Сумма, руб."]).round(2)
print(df[["Средневзвешенная ставка", "Сумма, руб."]])
