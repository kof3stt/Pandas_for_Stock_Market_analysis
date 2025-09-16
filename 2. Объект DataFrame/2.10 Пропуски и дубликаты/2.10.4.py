import pandas as pd
import numpy as np


df_values = [
    ["Nov 30, 2023", 2038.10, 25.29, 931.20],
    ["Nov 29, 2023", 2047.10, 25.07, 936.40],
    ["Nov 28, 2023", 2039.70, 24.93, 944.10],
    ["Nov 27, 2023", 2011.80, 24.67, 917.10],
    ["Nov 24, 2023", 2002.20, 24.33, 931.10],
    ["Nov 23, 2023", 1991.50, np.nan, np.nan],
    ["Nov 22, 2023", 1991.40, 23.67, 924.60],
    ["Nov 21, 2023", 1999.30, 23.84, 940.00],
    ["Nov 20, 2023", 1977.70, 23.58, 921.50],
    ["Nov 17, 2023", 1981.60, 23.81, 894.70],
    ["Nov 16, 2023", 1983.90, 23.89, 897.10],
    ["Nov 15, 2023", 1960.10, 23.48, 895.30],
]
df_columns = ["Date", "Gold", "Silver", "Platinum"]
df = pd.DataFrame(df_values, columns=df_columns).set_index("Date")
df.fillna(
    {"Silver": df["Silver"].mean(), "Platinum": df["Platinum"].mean()}, inplace=True
)
df["Silver"] = df["Silver"].round(2)
df["Platinum"] = df["Platinum"].round(2)
print(df)
