import pandas as pd


print(
    pd.bdate_range(
        start="2023-03",
        end="2023-04",
        freq="C",
        holidays=["2023-03-08"],
        weekmask="1111100",
    )
)
