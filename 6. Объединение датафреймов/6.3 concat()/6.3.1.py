import pandas as pd


baker_values_1 = [
    ["31.03.2023", 592],
    ["24.03.2023", 593],
    ["17.03.2023", 589],
    ["10.03.2023", 590],
    ["03.03.2023", 592],
    ["24.02.2023", 600],
    ["17.02.2023", 607],
    ["10.02.2023", 609],
    ["03.02.2023", 599],
    ["27.01.2023", 609],
    ["20.01.2023", 613],
    ["13.01.2023", 623],
    ["06.01.2023", 618],
]
baker_columns = ["Дата выпуска", "Факт."]
baker_1 = pd.DataFrame(baker_values_1, columns=baker_columns)
baker_values_2 = [
    ["30.06.2023", 545],
    ["23.06.2023", 546],
    ["16.06.2023", 552],
    ["09.06.2023", 556],
    ["02.06.2023", 555],
    ["26.05.2023", 570],
    ["19.05.2023", 575],
    ["12.05.2023", 586],
    ["05.05.2023", 588],
    ["28.04.2023", 591],
    ["21.04.2023", 591],
    ["14.04.2023", 588],
    ["06.04.2023", 590],
]
baker_2 = pd.DataFrame(baker_values_2, columns=baker_columns)
baker = pd.concat([baker_1, baker_2], ignore_index=True)
baker = baker.sort_values("Дата выпуска", ignore_index=True, key = lambda dt: pd.to_datetime(dt, format = "%d.%m.%Y"), ascending=False)
print(baker)
