import pandas as pd


d = {
    "BSPB": 'ПАО "Банк "Санкт-Петербург"',
    "CBOM": 'ПАО "МОСКОВСКИЙ КРЕДИТНЫЙ БАНК"',
    "ROSB": "ПАО РОСБАНК",
    "SBER": "ПАО Сбербанк",
    "USBN": 'ПАО "БАНК УРАЛСИБ"',
    "VTBR": "Банк ВТБ (ПАО)",
}
srs = pd.Series(d)
srs = pd.Series(data=srs.index, index=srs.values)
print(srs)
