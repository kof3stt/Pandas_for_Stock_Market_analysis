import pandas as pd


print(
    pd.Series(data=range(1, 8), index=[chr(i) for i in range(ord("a"), ord("g") + 1)])
)
