import pandas as pd
import numpy as np


pmi_manufacturing_russia_values = [
    ["01.07.2024 (июнь)", 54.9, np.nan, 54.4],
    ["03.06.2024 (май)", 54.4, np.nan, 54.3],
    ["02.05.2024 (апр)", 54.3, np.nan, 55.7],
    ["01.04.2024 (мар)", 55.7, np.nan, 54.7],
    ["01.03.2024 (фев)", 54.7, np.nan, 52.4],
    ["01.02.2024 (янв)", 52.4, np.nan, 54.6],
    ["29.12.2023 (дек)", 54.6, np.nan, 53.8],
    ["01.12.2023 (нояб)", 53.8, np.nan, 53.8],
    ["01.11.2023 (окт)", 53.8, np.nan, 54.5],
    ["02.10.2023 (сент)", 54.5, np.nan, 52.7],
    ["01.09.2023 (авг)", 52.7, np.nan, 52.1],
    ["01.08.2023 (июль)", 52.1, np.nan, 52.6],
    ["03.07.2023 (июнь)", 52.6, np.nan, 53.5],
    ["01.06.2023 (май)", 53.5, np.nan, 52.6],
    ["02.05.2023 (апр)", 52.6, np.nan, 53.2],
    ["03.04.2023 (мар)", 53.2, np.nan, 53.6],
    ["01.03.2023 (фев)", 53.6, np.nan, 52.6],
    ["01.02.2023 (янв)", 52.6, np.nan, 53.0],
]
pmi_manufacturing_russia_columns = ["Дата выпуска", "Факт.", "Прогноз", "Пред."]
pmi_manufacturing_russia = pd.DataFrame(
    pmi_manufacturing_russia_values, columns=pmi_manufacturing_russia_columns
)
pmi_manufacturing_russia.drop(columns=["Прогноз", "Пред."], inplace=True)
print(pmi_manufacturing_russia)
