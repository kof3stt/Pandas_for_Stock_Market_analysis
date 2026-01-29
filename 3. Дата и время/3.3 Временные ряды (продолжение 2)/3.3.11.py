import pandas as pd


index = pd.PeriodIndex(["2019-07", "2019-08", "2019-09"], freq="M")
print(index, type(index), sep="\n")
