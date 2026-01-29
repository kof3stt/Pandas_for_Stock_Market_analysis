import pandas as pd


df1 = pd.DataFrame(
    {
        "product_id": [1, 2, 3, 4],
        "product_name": ["Стол", "Кресло", "Лампа настольная", "Диван"],
    }
)

df2 = pd.DataFrame({"product_id": [1, 2, 4, 5], "price": [5000, 13000, 95000, 950]})
df = df1.merge(df2, how="left")
print(df)
