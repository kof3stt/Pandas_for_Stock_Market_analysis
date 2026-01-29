import pandas as pd


p = pd.Period("2014-12-01", freq="D")
p_modified = p - 30
print(p_modified, type(p_modified), sep="\n")
