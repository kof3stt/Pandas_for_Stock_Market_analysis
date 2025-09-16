import pandas as pd


gdp_2022_values = [
    ["United States", 25.46],
    ["China", 17.96],
    ["Japan", 4.23],
    ["Germany", 4.07],
    ["India", 3.38],
    ["United Kingdom", 3.07],
    ["France", 2.78],
    ["Russia", 2.24],
    ["Canada", 2.14],
    ["Italy", 2.01],
    ["Brazil", 1.92],
]
gdp_2022_columns = ["country", "gdp"]
print(pd.DataFrame(gdp_2022_values, columns=gdp_2022_columns))
