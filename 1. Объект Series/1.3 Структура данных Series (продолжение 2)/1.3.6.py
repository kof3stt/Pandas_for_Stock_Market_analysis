import pandas as pd


amounts = [300_000, 200_000, 500_000, 700_000, 1_000_000]
days = [30, 60, 90, 120, 180]
rates = [10, 11, 11, 12, 14]
amounts = pd.Series(amounts, name="Сумма депозита")
days = pd.Series(days, name="Дни")
rates = pd.Series(rates, name="Ставки")
srs = amounts * rates * days / 36500
print(srs.round(2))
