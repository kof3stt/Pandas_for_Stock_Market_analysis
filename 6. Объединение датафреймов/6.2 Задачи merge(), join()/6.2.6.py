import pandas as pd


df1 = pd.DataFrame(
    {
        "product_id": [103, 302, 257, 208],
        "product_name": ["Холодильник", "Кофемашина", "Наушники", "Парогенератор"],
    },
    index=[0, 3, 4, 5],
)

df2 = pd.DataFrame(
    {"country_of_origin": ["Russia", "China", "Russia", "Japan"]}, index=[0, 3, 4, 5]
)

df3 = pd.DataFrame(
    {
        "guarantee": ["да", "нет", "да", "да"],
        "guarantee_period": ["1 год", "0", "1,5 года", "1 год"],
    },
    index=[0, 3, 4, 5],
)
df = df1.join([df2, df3])
print(df)
