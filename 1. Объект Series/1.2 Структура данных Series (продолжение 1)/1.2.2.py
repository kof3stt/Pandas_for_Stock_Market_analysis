import pandas as pd
import numpy as np


arr = np.array([84.1375, 91.6525, 11.7650])
indx = ["usd/rub", "eur/rub", "cny/rub"]
srs = pd.Series(arr, index=indx)
srs.name = "Валюты"
srs.index.name = "Валютная пара"
print(srs)
