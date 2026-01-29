import pandas as pd


df1 = pd.DataFrame(
    {
        "id": [2, 4, 7, 8, 12, 13],
        "товар": [
            "ложка столовая",
            "нож",
            "вилка",
            "ложка чайная",
            "тарелка",
            "кружка",
        ],
        "количество": [1220, 2035, 890, 538, 240, 440],
    }
)

df2 = pd.DataFrame({"id": [2, 4, 7, 10, 12], "цена": [100, 450, 140, 280, 390]})
df1 = df1.set_index("id")
df2 = df2.set_index("id")
df = df1.join(df2, how="inner")
print(df)
