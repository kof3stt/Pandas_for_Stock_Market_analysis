import pandas as pd


df1 = pd.DataFrame(
    {
        "id": [1, 2, 3, 4],
        "name": ["Петров А.И.", "Смолин С.В.", "Иванова Е.Г.", "Антонова Н.Р."],
    }
)

df2 = pd.DataFrame({"id": [3, 4, 5, 6], "age": [23, 34, 45, 56]})
df = df1.merge(df2)
print(df)
