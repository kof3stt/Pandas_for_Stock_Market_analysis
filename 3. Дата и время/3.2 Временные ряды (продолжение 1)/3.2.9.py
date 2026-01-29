import pandas as pd


print(pd.bdate_range(start="1990", end="1991", freq="C", weekmask="1000000"))
