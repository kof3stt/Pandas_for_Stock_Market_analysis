import pandas as pd


d = {
    "Moody's": "США",
    "Standard & Poor's": "США",
    "Fitch Ratings": "США",
    "АКРА": "Россия",
    "Эксперт РА": "Россия",
    "НРА": "Россия",
}
srs = pd.Series(d)
srs.drop(["Moody's", "Standard & Poor's", "Fitch Ratings"], inplace=True)
print(srs)
