import pandas as pd


data = {
    "2019": 9564222000,
    "2020": 32993292000,
    "2021": 48105862000,
    "2022": 27932517000,
    "2023": 58677601000,
    "2024": 44333844000,
}
srs = pd.Series(data, dtype="float64")
srs = srs.astype("int64")
print(srs, srs.dtype, sep="\n\n")
