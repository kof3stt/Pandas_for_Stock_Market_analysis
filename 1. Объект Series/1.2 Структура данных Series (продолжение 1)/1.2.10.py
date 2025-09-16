import pandas as pd


d = {
    "BANE": 'ПАО АНК "Башнефть"',
    "LKOH": 'ПАО "ЛУКОЙЛ"',
    "NVTK": 'ПАО "НОВАТЭК"',
    "ROSN": 'ПАО "НК "Роснефть"',
    "TATN": 'ПАО "Татнефть" им. В.Д.Шашина',
    "TRNFL": 'ПАО "Транснефть"',
}
srs = pd.Series(d)
srs["GAZP"] = 'ПАО "Газпром"'
srs["SIBN"] = 'ПАО "Газпром нефть"'
srs["SNGS"] = 'ПАО "Сургутнефтегаз"'
print(srs, srs.index, srs.values, sep="\n\n")
