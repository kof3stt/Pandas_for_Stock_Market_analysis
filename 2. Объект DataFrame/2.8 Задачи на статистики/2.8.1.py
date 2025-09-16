import pandas as pd


depo_values = [
    ["New Energy Bank", 500_000_000, 8.15, "П", "O/N"],
    ["AgroFoodBank", 1_000_000_000, 8.20, "П", "O/N"],
    ["First Ecologic Bank", 400_000_000, 8.11, "П", "O/N"],
    ["Cryptocurrencybank", 700_000_000, 8.15, "П", "O/N"],
    ["Big Business Bank", 2_600_000_000, 8.30, "Р", "O/N"],
    ["SmallBusinessBank", 2_000_000_000, 8.20, "П", "O/N"],
    ["GreenEnergyBank", 1_000_000_000, 8.10, "П", "O/N"],
    ["Allmoneybank", 3_000_000_000, 8.27, "Р", "O/N"],
    ["ClearWaterBank", 300_000_000, 8.00, "П", "O/N"],
    ["First Ecologic Bank", 700_000_000, 8.15, "П", "O/N"],
    ["Cryptocurrencybank", 500_000_000, 8.15, "П", "O/N"],
    ["Allmoneybank", 1_500_000_000, 8.20, "Р", "O/N"],
    ["Golden Silver Bank", 800_000_000, 8.05, "П", "O/N"],
    ["New Energy Bank", 300_000_000, 8.00, "П", "O/N"],
    ["AgroFoodBank", 400_000_000, 8.00, "П", "O/N"],
    ["Golden Silver Bank", 500_000_000, 8.03, "П", "O/N"],
    ["SmallBusinessBank", 400_000_000, 8.00, "П", "O/N"],
    ["New Energy Bank", 500_000_000, 7.90, "П", "O/N"],
    ["Big Business Bank", 2_900_000_000, 8.15, "Р", "O/N"],
]
depo_columns = ["Банк", "Сумма, руб.", "Ставка", "Направление", "Срок"]
depo = pd.DataFrame(depo_values, columns=depo_columns)
depo["Проценты"] = (depo["Сумма, руб."] * depo["Ставка"] / 36500).round(2)
depo["Проценты"].where(
    depo["Направление"] != "П", -depo["Проценты"], axis=0, inplace=True
)
print(depo, depo["Проценты"].sum().round(2), sep="\n\n")
