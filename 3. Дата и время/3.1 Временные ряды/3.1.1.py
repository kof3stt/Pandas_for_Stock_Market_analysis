import pandas as pd


s = input()
timestamp = pd.Timestamp(s)
print(timestamp, type(timestamp), sep="\n")
