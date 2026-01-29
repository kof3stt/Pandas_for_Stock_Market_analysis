import pandas as pd


df1 = pd.DataFrame(
    {
        "id_сотрудника": [10, 2, 37, 51],
        "отдел": ["HR", "IT", "Отдел маркетинга", "Отдел продаж"],
    }
)

df2 = pd.DataFrame({"id_сотрудника": [2, 37, 44], "оклад": [50000, 60000, 70000]})
df = df1.merge(df2, on="id_сотрудника", how="outer", sort=True)
print(df)
