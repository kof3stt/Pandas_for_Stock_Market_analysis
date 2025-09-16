import pandas as pd


d = {
    "AMEZ": 'ПАО "Ашинский метзавод"',
    "CHMF": 'ПАО "Северсталь"',
    "CHMK": 'ПАО "ЧМК"',
    "GMKN": 'ПАО "ГМК "Норильский никель"',
    "MAGN": 'ПАО "ММК"',
    "MTLR": 'ПАО "Мечел"',
    "NLMK": 'ПАО "НЛМК"',
    "RUAL": 'МКПАО "ОК РУСАЛ"',
    "TRMK": 'ПАО "ТМК"',
}
srs = pd.Series(d)
srs.drop(list(d.keys())[1::2], inplace=True)
print(srs)
