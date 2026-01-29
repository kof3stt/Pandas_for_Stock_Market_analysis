import pandas as pd


period = pd.Period("2022-06", freq="M")
print(period, type(period), sep="\n")
