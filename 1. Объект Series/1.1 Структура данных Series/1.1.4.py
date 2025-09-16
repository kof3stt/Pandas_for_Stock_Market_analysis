import pandas as pd


names = [
    "Биткоин",
    "Эфириум",
    "Tether USDt",
    "BNB",
    "XRP",
    "Solana",
    "USD Coin",
    "Lido Staked ETH",
    "Cardano",
    "Dogecoin",
]
values = ["BTC", "ETH", "USDT", "BNB", "XRP", "SOL", "USDC", "stETH", "ADA", "DOGE"]


print(pd.Series(data=values, index=names).index)
