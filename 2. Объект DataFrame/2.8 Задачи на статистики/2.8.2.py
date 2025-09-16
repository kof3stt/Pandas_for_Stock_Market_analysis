import pandas as pd


depo_values = [
    ["New Energy Bank", 1_000_000_000, 8.30, "O/N"],
    ["Cryptocurrencybank", 2_700_000_000, 8.35, "O/N"],
    ["Big Business Bank", 1_500_000_000, 8.27, "O/N"],
    ["GreenEnergyBank", 1_800_000_000, 8.35, "O/N"],
    ["Allmoneybank", 5_900_000_000, 8.45, "O/N"],
    ["ClearWaterBank", 3_000_000_000, 8.40, "O/N"],
    ["First Ecologic Bank", 3_000_000_000, 8.41, "O/N"],
    ["Cryptocurrencybank", 7_500_000_000, 8.50, "O/N"],
    ["Big Business Bank", 2_500_000_000, 8.35, "O/N"],
    ["AgroFoodBank", 700_000_000, 8.25, "O/N"],
    ["Golden Silver Bank", 4_300_000_000, 8.42, "O/N"],
    ["SmallBusinessBank", 2_000_000_000, 8.31, "O/N"],
]
depo_columns = ["Банк", "Сумма, руб.", "Ставка", "Срок"]
depo = pd.DataFrame(depo_values, columns=depo_columns)
print(
    ((depo["Сумма, руб."] * depo["Ставка"]).sum() / depo["Сумма, руб."].sum()).round(2)
)
