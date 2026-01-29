import pandas as pd


s = input()
ts = pd.Timestamp(s)
print(ts)
print(type(ts))
print()
str_ts = ts.strftime("%d.%m.%y")
print(str_ts, type(str_ts), sep="\n")
