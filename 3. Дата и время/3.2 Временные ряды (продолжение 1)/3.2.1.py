import pandas as pd
from datetime import datetime


format = "%d.%m.%Y"
print(
    pd.date_range(
        start=datetime.strptime("27.02.2023", format),
        end=datetime.strptime("03.03.2023", format),
    )
)
