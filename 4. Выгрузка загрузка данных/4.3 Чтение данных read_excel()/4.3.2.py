import pandas as pd


for i in range(18, 23):
    df = pd.read_excel(f"USD000UTSTOM_{i}0101_{i}1231.xlsx", usecols=["<CLOSE>"]).iloc[
        :, 0
    ]
    print(f"20{i}: {df.mean().round(4)}")
