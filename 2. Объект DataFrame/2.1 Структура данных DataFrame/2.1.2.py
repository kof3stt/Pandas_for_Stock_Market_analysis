import pandas as pd


gdp_2022 = {
    "country": [
        "United States",
        "China",
        "Japan",
        "Germany",
        "India",
        "United Kingdom",
        "France",
        "Russia",
        "Canada",
        "Italy",
        "Brazil",
    ],
    "gdp": [25.46, 17.96, 4.23, 4.07, 3.38, 3.07, 2.78, 2.24, 2.14, 2.01, 1.92],
}
print(pd.DataFrame(gdp_2022))
