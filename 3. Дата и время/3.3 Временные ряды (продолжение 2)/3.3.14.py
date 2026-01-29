import pandas as pd


gdp_china = ["4,8%", "0,4%", "3,9%", "2,9%", "4,5%", "6,3%"]
print(pd.Series(gdp_china, index=pd.period_range("2022Q1", periods=6, freq="Q")))
