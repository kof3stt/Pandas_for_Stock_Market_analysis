import pandas as pd


print(
    pd.date_range(
        start="2023-10-01 08", end="2023-10-01 20", freq="H", tz="America/New_York"
    )
)
