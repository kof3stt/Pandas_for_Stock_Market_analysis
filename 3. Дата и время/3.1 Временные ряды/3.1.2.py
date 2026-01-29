import pandas as pd


timestamp = pd.to_datetime(input(), format="%m/%d/%y %H:%M:%S")
print(timestamp, type(timestamp), sep="\n")
