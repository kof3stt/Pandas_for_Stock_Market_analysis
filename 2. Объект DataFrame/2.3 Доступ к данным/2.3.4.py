import pandas as pd


depo_values = [
    ["New Energy Bank", 1_000_000_000, 8.30, "O/N"],
    ["AgroFoodBank", 5_000_000_000, 8.50, "1W"],
    ["First Ecologic Bank", 4_500_000_000, 8.60, "1M"],
    ["Cryptocurrencybank", 2_700_000_000, 8.30, "O/N"],
    ["GreenEnergyBank", 1_800_000_000, 8.35, "O/N"],
    ["ClearWaterBank", 3_000_000_000, 8.40, "O/N"],
    ["Cryptocurrencybank", 7_500_000_000, 8.50, "O/N"],
    ["New Energy Bank", 2_000_000_000, 8.45, "1W"],
    ["AgroFoodBank", 700_000_000, 8.25, "O/N"],
    ["Golden Silver Bank", 4_300_000_000, 8.40, "O/N"],
    ["New Energy Bank", 4_000_000_000, 8.80, "3M"],
]
depo_columns = ["Банк", "Сумма, руб.", "Ставка", "Срок"]
depo = pd.DataFrame(depo_values, columns=depo_columns)
print(depo[depo["Срок"] == "O/N"])
