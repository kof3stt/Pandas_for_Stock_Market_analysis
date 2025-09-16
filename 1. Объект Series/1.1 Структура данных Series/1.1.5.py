import pandas as pd


years = range(2018, 2025)
data = [
    31837000000,
    643000000,
    46607000000,
    42078000000,
    19325000000,
    32104000000,
    -61162000000,
]
print(pd.Series(data=data, index=years))
