import pandas as pd


index = pd.period_range("2023-04-01", "2023-04-10")
print(index, type(index), sep="\n")
