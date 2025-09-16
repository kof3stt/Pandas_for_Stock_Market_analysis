import pandas as pd


unemployment_values = [
    ["январь", 5.6, 5.2, 4.9, 4.7, 5.8, 4.4, 3.6],
    ["февраль", 5.6, 5.0, 4.9, 4.6, 5.7, 4.1, 3.49],
    ["март", 5.4, 5.0, 4.7, 4.7, 5.4, 4.1, 3.5],
]
unemployment_columns = ["месяц", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
unemployment = pd.DataFrame(unemployment_values, columns=unemployment_columns)
unemployment.set_index("месяц", inplace=True)
unemployment = unemployment.transpose()
print(unemployment)
