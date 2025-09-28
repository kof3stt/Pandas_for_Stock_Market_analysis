import pandas as pd
from datetime import datetime


def convert_columns(date_str):
    date, month_name = date_str.split()
    _, month, year = date.split(".")
    if month == "01":
        year = str(int(year) - 1)
    return datetime.strptime(date, "%d.%m.%Y"), month_name.strip("()") + " " + year


pmi_manufacturing_turkey_values = [
    ["03.07.2023 (июнь)", 51.5],
    ["01.06.2023 (май)", 51.5],
    ["02.05.2023 (апр)", 51.5],
    ["03.04.2023 (мар)", 50.9],
    ["01.03.2023 (фев)", 50.1],
    ["01.02.2023 (янв)", 50.1],
    ["02.01.2023 (дек)", 48.1],
    ["01.12.2022 (нояб)", 45.7],
    ["01.11.2022 (окт)", 46.4],
    ["03.10.2022 (сент)", 46.9],
    ["01.09.2022 (авг)", 47.4],
    ["01.08.2022 (июль)", 46.9],
    ["01.07.2022 (июнь)", 48.1],
    ["01.06.2022 (май)", 49.2],
    ["05.05.2022 (апр)", 49.2],
    ["01.04.2022 (мар)", 49.4],
    ["01.03.2022 (фев)", 50.4],
    ["01.02.2022 (янв)", 50.5],
    ["03.01.2022 (дек)", 52.1],
    ["01.12.2021 (нояб)", 52.0],
    ["01.11.2021 (окт)", 51.2],
    ["01.10.2021 (сент)", 52.5],
    ["01.09.2021 (авг)", 54.1],
    ["02.08.2021 (июль)", 54.0],
    ["01.07.2021 (июнь)", 51.3],
    ["01.06.2021 (май)", 49.3],
    ["03.05.2021 (апр)", 50.4],
    ["01.04.2021 (мар)", 52.6],
    ["01.03.2021 (фев)", 51.7],
    ["01.02.2021 (янв)", 54.4],
]
pmi_manufacturing_turkey_columns = ["Дата выпуска", "Факт."]
pmi_manufacturing_turkey = pd.DataFrame(
    pmi_manufacturing_turkey_values, columns=pmi_manufacturing_turkey_columns
)
pmi_manufacturing_turkey[["Дата выпуска", "Период"]] = pmi_manufacturing_turkey[
    "Дата выпуска"
].apply(lambda x: pd.Series(convert_columns(x)))
pmi_manufacturing_turkey = pmi_manufacturing_turkey[["Дата выпуска", "Период", "Факт."]]
print(pmi_manufacturing_turkey, end="\n\n")
pmi_manufacturing_turkey.info()
