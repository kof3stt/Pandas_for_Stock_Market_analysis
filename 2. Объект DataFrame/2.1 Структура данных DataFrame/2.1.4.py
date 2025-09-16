import pandas as pd


gdp_2022 = [
    {"country": "United States", "gdp": 25.46},
    {"country": "China", "gdp": 17.96},
    {"country": "Japan", "gdp": 4.23},
    {"country": "Germany", "gdp": 4.07},
    {"country": "India", "gdp": 3.38},
    {"country": "United Kingdom", "gdp": 3.07},
    {"country": "France", "gdp": 2.78},
    {"country": "Russia", "gdp": 2.24},
    {"country": "Canada", "gdp": 2.14},
    {"country": "Italy", "gdp": 2.01},
    {"country": "Brazil", "gdp": 1.92},
]
print(pd.DataFrame(gdp_2022))
