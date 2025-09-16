import pandas as pd


df_values = [
    ["S&P 500", "Dec 01, 2023", "4,559.43", "4,594.63"],
    ["NASDAQ Composite", "Dec 01, 2023", "14,181.35", "14,305.03"],
    ["Dow Jones Industrial Average", "Dec 01, 2023", "35,914.45", "36,245.50"],
    ["S&P 500", "Nov 30, 2023", "4,554.87", "4,567.80"],
    ["NASDAQ Composite", "Nov 30, 2023", "14,265.05", "14,226.22"],
    ["Dow Jones Industrial Average", "Nov 30, 2023", "35,596.57", "35,950.89"],
    ["S&P 500", "Nov 29, 2023", "4,571.84", "4,550.58"],
    ["NASDAQ Composite", "Nov 29, 2023", "14,367.11", "14,258.49"],
    ["Dow Jones Industrial Average", "Nov 29, 2023", "35,436.80", "35,430.42"],
    ["S&P 500", "Nov 28, 2023", "4,545.55", "4,554.89"],
    ["NASDAQ Composite", "Nov 28, 2023", "14,224.63", "14,281.76"],
    ["Dow Jones Industrial Average", "Nov 28, 2023", "35,332.13", "35,416.98"],
    ["S&P 500", "Nov 27, 2023", "4,554.86", "4,550.43"],
    ["NASDAQ Composite", "Nov 27, 2023", "14,239.31", "14,241.02"],
    ["Dow Jones Industrial Average", "Nov 27, 2023", "35,376.44", "35,333.47"],
]
df_columns = ["Exchange Index", "Date", "Open", "Close"]
df = pd.DataFrame(df_values, columns=df_columns)
df.set_index("Exchange Index", inplace=True)
print(df.query('Date == "Nov 29, 2023"'))
