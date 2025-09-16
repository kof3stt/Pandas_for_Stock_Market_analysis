import pandas as pd
import numpy as np


moscow_exchange_values = [
    ["2023-03-10", 2276.25, 2272.61, 2283.18, 2266.33, -0.61, np.nan, np.nan],
    ["2023-03-09", 2290.14, 2295.03, 2302.1, 2278.95, -0.24, np.nan, np.nan],
    ["2023-03-07", 2295.6, 2294.32, 2298.93, 2281.46, 0.06, np.nan, np.nan],
    ["2023-03-06", 2294.12, 2286.2, 2297.86, 2283.4, 0.96, np.nan, np.nan],
    ["2023-03-03", 2272.2, 2250.12, 2273.52, 2249.81, 0.79, np.nan, np.nan],
    ["2023-03-02", 2254.3, 2284.87, 2286.27, 2235.43, -1.11, np.nan, np.nan],
    ["2023-03-01", 2279.65, 2258.89, 2287.48, 2255.45, 1.18, np.nan, np.nan],
]
moscow_exchange_columns = [
    "Дата",
    "Цена",
    "Откр.",
    "Макс.",
    "Мин.",
    "Изм. %",
    "Unnamed: 6",
    "Unnamed: 7",
]
moex = pd.DataFrame(moscow_exchange_values, columns=moscow_exchange_columns)
moex.drop(["Unnamed: 6", "Unnamed: 7"], axis=1, inplace=True)
print(moex)
