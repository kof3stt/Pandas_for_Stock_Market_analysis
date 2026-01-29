import pandas as pd


s = input()
ts = pd.Timestamp(s)
print(ts)
print(type(ts))
print()
print(ts.to_datetime64())
print(type(ts.to_datetime64()))
