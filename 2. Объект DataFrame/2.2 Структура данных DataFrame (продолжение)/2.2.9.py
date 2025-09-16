import pandas as pd


srs1 = pd.Series(
    [
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
    name="country",
)
srs2 = pd.Series(
    [25.46, 17.96, 4.23, 4.07, 3.38, 3.07, 2.78, 2.24, 2.14, 2.01, 1.92], name="gdp"
)
df = pd.DataFrame([srs1, srs2]).transpose()
print(df)
