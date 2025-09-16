import pandas as pd
import numpy as np


currency_values = [
    ["USDRUB_TOM", "buy", 1_000_000, 96.80],
    ["USDRUB_TOM", "sell", 100_000, 96.90],
    ["USDRUB_TOM", "sell", 200_000, 97.20],
    ["USDRUB_TOM", "sell", 500_000, 97.50],
    ["USDRUB_TOM", "sell", 200_000, 97.30],
    ["USDRUB_TOM", "buy", 2_000_000, 97.00],
    ["USDRUB_TOM", "buy", 5_000_000, 96.85],
    ["USDRUB_TOM", "sell", 1_000_000, 97.05],
    ["USDRUB_TOM", "sell", 1_000_000, 97.10],
    ["USDRUB_TOM", "sell", 1_000_000, 97.15],
    ["USDRUB_TOM", "sell", 1_000_000, 97.20],
    ["USDRUB_TOM", "sell", 1_000_000, 97.25],
]
currency_columns = ["Валюта", "Направление сделки", "Объем валюты", "Цена"]
currency = pd.DataFrame(currency_values, columns=currency_columns)
mask_buy = currency["Направление сделки"].isin(["buy"])
mask_sell = currency["Направление сделки"].isin(["sell"])
total_buy = currency[mask_buy]["Объем валюты"].sum()
total_sell = currency[mask_sell]["Объем валюты"].sum()
wa_buy = (
    currency[mask_buy]["Объем валюты"] * currency[mask_buy]["Цена"]
).sum() / total_buy
wa_sell = (
    currency[mask_sell]["Объем валюты"] * currency[mask_sell]["Цена"]
).sum() / total_sell
print(f"Куплено {total_buy} USDRUB_TOM по курсу {wa_buy.round(4)}")
print(f"Продано {total_sell} USDRUB_TOM по курсу {wa_sell.round(4)}")
