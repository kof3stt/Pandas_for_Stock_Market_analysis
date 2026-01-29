import pandas as pd


orders_df = pd.DataFrame(
    {
        "order_id": [1254, 1255, 1256, 1257],
        "product_id": [103, 302, 257, 208],
        "client_id": [1001, 1002, 1003, 1004],
        "order_date": ["2024-07-10", "2024-07-11", "2024-07-12", "2024-07-12"],
    }
)

products_df = pd.DataFrame(
    {"product_id": [103, 208], "product_name": ["Холодильник", "Парогенератор"]}
)

clients_df = pd.DataFrame(
    {
        "client_id": [1001, 1002, 1003, 1004],
        "client_name": [
            "Алексеев С.А.",
            "Семенов Н.Д.",
            "Петрова Л.С.",
            "Боброва А.Г.",
        ],
    }
)
df = orders_df.merge(products_df, how="inner").merge(clients_df, how="inner")
print(df)
