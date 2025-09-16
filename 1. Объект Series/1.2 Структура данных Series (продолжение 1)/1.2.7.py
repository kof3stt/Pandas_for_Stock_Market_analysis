import pandas as pd
import numpy as np


d = {
    "2017": 78616000000,
    "2018": 90404000000,
    "2019": 62730000000,
    "2020": 32245000000,
    "2021": np.nan,
}
srs = pd.Series(d)
srs["2021"] = 91319000000
srs = srs.astype(dtype="int64")
print(srs)
