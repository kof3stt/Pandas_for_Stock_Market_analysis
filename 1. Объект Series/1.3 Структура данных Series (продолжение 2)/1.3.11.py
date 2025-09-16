import pandas as pd


srs = pd.Series(data=map(int, input().split()))
srs = srs ** (srs.index + 1)
print(srs)
