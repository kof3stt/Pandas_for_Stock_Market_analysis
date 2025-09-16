import pandas as pd


lst1 = [
    "2023-01-01",
    "2023-02-01",
    "2023-03-01",
    "2023-04-01",
    "2023-05-01",
    "2023-06-01",
    "2023-07-01",
    "2023-08-01",
]
srs1 = pd.Series(lst1, dtype="datetime64[ns]")
srs2 = pd.Series("2020-01-01", index=range(8), dtype="datetime64[ns]")
srs = pd.Series(srs1 - srs2, dtype="timedelta64[ns]")
print(srs)
