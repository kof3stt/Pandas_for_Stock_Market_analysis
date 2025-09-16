import pandas as pd


s = list(map(int, input().split()))
srs = pd.Series(data=s)
print(srs)
