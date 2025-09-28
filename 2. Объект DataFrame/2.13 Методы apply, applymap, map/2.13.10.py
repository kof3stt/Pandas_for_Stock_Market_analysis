import pandas as pd


depo_values = [
    ["New Energy Bank", 1_000_000_000, 8.30, "O/N"],
    ["AgroFoodBank", 5_000_000_000, 8.50, "1W"],
    ["First Ecologic Bank", 4_500_000_000, 8.60, "1M"],
    ["Cryptocurrencybank", 2_700_000_000, 8.30, "O/N"],
    ["Big Business Bank", 1_500_000_000, 8.27, "O/N"],
    ["GreenEnergyBank", 1_800_000_000, 8.35, "O/N"],
    ["Allmoneybank", 5_900_000_000, 8.45, "O/N"],
    ["ClearWaterBank", 3_000_000_000, 8.40, "O/N"],
    ["First Ecologic Bank", 3_000_000_000, 8.41, "O/N"],
    ["Cryptocurrencybank", 7_500_000_000, 8.50, "O/N"],
    ["Allmoneybank", 2_400_000_000, 9.00, "3M"],
    ["Big Business Bank", 2_500_000_000, 8.30, "O/N"],
    ["Golden Silver Bank", 2_500_000_000, 8.65, "1M"],
    ["New Energy Bank", 2_000_000_000, 8.45, "1W"],
    ["AgroFoodBank", 700_000_000, 8.25, "O/N"],
    ["Golden Silver Bank", 4_300_000_000, 8.40, "O/N"],
    ["SmallBusinessBank", 2_000_000_000, 8.31, "O/N"],
    ["SmallBusinessBank", 8_000_000_000, 8.70, "1M"],
    ["New Energy Bank", 4_000_000_000, 8.80, "3M"],
]
depo_columns = ["Банк", "Сумма, руб.", "Ставка", "Срок"]
depo = pd.DataFrame(depo_values, columns=depo_columns)
key_dict = {"O/N": 1, "1W": 7, "1M": 30, "3M": 90}
depo["Количество дней"] = depo["Срок"].apply(lambda x: key_dict[x])
print(depo)
