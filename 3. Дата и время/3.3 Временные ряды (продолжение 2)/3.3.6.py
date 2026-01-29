import pandas as pd


ts1, ts2 = [pd.Timestamp(input()) for _ in range(2)]
result = ts2 - ts1
print(result, type(result), sep="\n")
