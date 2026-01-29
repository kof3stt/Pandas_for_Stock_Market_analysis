import pandas as pd


pri = pd.period_range(start="2023-09-04", periods=3, freq="D")
pri_modified = pri + 7
print(pri_modified, type(pri_modified), sep="\n")
