import pandas as pd


p = pd.Period("2020-05-05", freq="H")
p_modified = p + 50
print(p_modified, type(p_modified), sep="\n")
