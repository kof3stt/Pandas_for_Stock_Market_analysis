import pandas as pd


print(pd.date_range(start=pd.Timestamp("2023-09-01 10"), freq="H", periods=12))
