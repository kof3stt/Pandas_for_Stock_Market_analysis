import pandas as pd


orders_df = pd.DataFrame(
    {
        "order_id": [1254, 1255, 1256],
        "product_id": [103, 302, 257],
        "client_id": [1001, 1002, 1003],
        "order_date": ["2024-07-10", "2024-07-11", "2024-07-12"],
    }
)

products_df = pd.DataFrame(
    {
        "product_id": [103, 302, 257],
        "product_name": ["Холодильник", "Кофемашина", "Наушники"],
    }
)

clients_df = pd.DataFrame(
    {
        "client_id": [1001, 1002, 1003],
        "client_name": ["Алексеев С.А.", "Семенов Н.Д.", "Петрова Л.С."],
    }
)
df = orders_df.merge(products_df, on="product_id", how="inner").merge(
    clients_df, on="client_id", how="inner"
)
print(df)
