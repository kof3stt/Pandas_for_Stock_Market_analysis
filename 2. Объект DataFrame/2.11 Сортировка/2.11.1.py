import pandas as pd
import numpy as np


exchanges_values = [
    [
        "Нью-Йоркская биржа New York Stock Exchange(NYSE)",
        "США",
        "1817",
        "Dow Jones, NYSE Composite, S&P500",
        "доллар США",
        "фондовый, срочный, товарный",
    ],
    [
        "Чикагская биржа (CME)",
        "США",
        "1874",
        np.nan,
        "доллар США",
        "товарный, валютный, рынок драгоценных металлов, срочный",
    ],
    [
        "NASDAQ (National Association of Securities Dealers Automated Quotation)",
        "США",
        "1971",
        "NASDAQ Composite, NASDAQ-100, S&P500",
        "доллар США",
        "фондовый, срочный",
    ],
    [
        "Лондонская биржа London Stock Exchange (LSE)",
        "Великобритания",
        "1698",
        "FTSE 100",
        "английский фунт",
        "фондовый, срочный",
    ],
    [
        "Japan Exchange Group (JPX)",
        "Япония",
        "1878",
        "NIKKEI 225",
        "японская йена",
        "фондовый, срочный",
    ],
    [
        "Гонконгская биржа Hong Kong Stock Exchange (HKEX)",
        "Китай",
        "1891",
        "Hang Seng",
        "гонконгский доллар",
        "фондовый, срочный",
    ],
    ["Deutsche Börse", "Германия", "1585", "DAX", "евро", "фондовый, срочный"],
    [
        "Euronext",
        "Европейский союз",
        "2000",
        "Euronext 100, CAC 40",
        "евро",
        "фондовый, срочный",
    ],
    [
        "Шанхайская биржа Shanghai Stock Exchange (SSE)",
        "Китай",
        "1860",
        "SSE Composite",
        "китайский юань",
        "фондовый, срочный",
    ],
    [
        "Шэньчжэньская фондовая биржа Shenzhen Stock Exchange (SZSE)",
        "Китай",
        "1990",
        "SZSE Component",
        "китайский юань",
        "фондовый, срочный",
    ],
    [
        "Национальная фондовая биржа Индии National Stock Exchange of India (NSE)",
        "Индия",
        "1992",
        "NIFTY 50",
        "индийская рупия",
        "фондовый, срочный",
    ],
    [
        "Бомбейская фондовая биржа Bombay Stock Exchange (BSE)",
        "Индия",
        "1875",
        "BSE SENSEX",
        "индийская рупия",
        "фондовый, срочный",
    ],
]
exchanges_columns = [
    "Наименование биржи",
    "Страна",
    "Год основания",
    "Индексы",
    "Валюта",
    "Рынки",
]
exchanges = pd.DataFrame(exchanges_values, columns=exchanges_columns)
exchanges.sort_values(by=["Страна", "Год основания"], inplace=True)
print(exchanges[["Наименование биржи", "Год основания"]])
