import pandas as pd


baker_values_april = [
    ["28.04.2023", 591],
    ["21.04.2023", 591],
    ["14.04.2023", 588],
    ["06.04.2023", 590],
]
baker_values_may = [
    ["26.05.2023", 570],
    ["19.05.2023", 575],
    ["12.05.2023", 586],
    ["05.05.2023", 588],
]
baker_values_june = [
    ["30.06.2023", 545],
    ["23.06.2023", 546],
    ["16.06.2023", 552],
    ["09.06.2023", 556],
    ["02.06.2023", 555],
]
baker_columns = ["Дата выпуска", "Факт."]
baker_april = pd.DataFrame(baker_values_april, columns=baker_columns)
baker_may = pd.DataFrame(baker_values_may, columns=baker_columns)
baker_june = pd.DataFrame(baker_values_june, columns=baker_columns)
baker = pd.concat(
    [baker_june, baker_may, baker_april], keys=["июнь 2023", "май 2023", "апрель 2023"]
)
print(baker)
