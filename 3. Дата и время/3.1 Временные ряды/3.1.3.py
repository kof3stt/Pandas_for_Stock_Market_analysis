import pandas as pd


timestamp = pd.to_datetime(input(), format="%d.%m.%Y")
print(timestamp, type(timestamp), sep="\n")
