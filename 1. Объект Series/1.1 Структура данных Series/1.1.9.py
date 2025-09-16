import pandas as pd


dates = [
    "2023-03-01",
    "2023-03-02",
    "2023-03-03",
    "2023-03-06",
    "2023-03-07",
    "2023-03-09",
    "2023-03-10",
]
srs = pd.Series(dates, dtype="datetime64[ns]")
print(srs)
