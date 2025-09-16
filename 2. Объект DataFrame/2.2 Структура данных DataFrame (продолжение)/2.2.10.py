import pandas as pd


unemployment_values = [
    ["January", 5.6, 5.2, 4.9, 4.7, 5.8, 4.4],
    ["February", 5.6, 5.0, 4.9, 4.6, 5.7, 4.1],
    ["March", 5.4, 5.0, 4.7, 4.7, 5.4, 4.1],
    ["April", 5.3, 4.9, 4.7, 5.8, 5.2, 4.0],
    ["May", 5.2, 4.7, 4.5, 6.1, 4.9, 3.9],
    ["June", 5.1, 4.7, 4.4, 6.2, 4.8, 3.9],
    ["July", 5.1, 4.7, 4.5, 6.3, 4.5, 3.9],
    ["August", 4.9, 4.6, 4.3, 6.4, 4.4, 3.8],
    ["September", 5.0, 4.5, 4.5, 6.3, 4.3, 3.9],
    ["October", 5.0, 4.7, 4.6, 6.3, 4.3, 3.9],
    ["November", 5.1, 4.8, 4.6, 6.1, 4.3, 3.7],
    ["December", 5.1, 4.8, 4.6, 5.9, 4.3, 3.7],
]
unemployment_columns = ["месяц", "2017", "2018", "2019", "2020", "2021", "2022"]
unemployment = pd.DataFrame(unemployment_values, columns=unemployment_columns)
unemployment.rename({"месяц": "month"}, inplace=True, axis="columns")
print(unemployment)
