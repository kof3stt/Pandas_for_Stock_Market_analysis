import pandas as pd


alibaba_values = [
    ["03.07.2023", 84.87, 84.07],
    ["05.07.2023", 83.98, 84.30],
    ["06.07.2023", 83.12, 83.84],
    ["07.07.2023", 86.76, 90.55],
    ["10.07.2023", 90.05, 90.56],
    ["11.07.2023", 91.02, 91.79],
    ["12.07.2023", 94.11, 94.00],
    ["13.07.2023", 95.03, 96.61],
    ["14.07.2023", 95.22, 94.56],
    ["17.07.2023", 92.25, 93.41],
    ["18.07.2023", 91.54, 91.20],
    ["19.07.2023", 93.57, 92.09],
    ["20.07.2023", 91.69, 91.90],
    ["21.07.2023", 92.89, 92.17],
    ["24.07.2023", 92.07, 96.35],
    ["25.07.2023", 98.17, 94.98],
    ["26.07.2023", 94.95, 97.14],
    ["27.07.2023", 97.75, 95.44],
    ["28.07.2023", 98.07, 100.55],
    ["31.07.2023", 99.79, 102.16],
]
alibaba_columns = ["Date", "Open", "Close"]
alibaba = pd.DataFrame(alibaba_values, columns=alibaba_columns)
alibaba = alibaba.set_index(pd.to_datetime(alibaba["Date"], dayfirst=True))
alibaba = alibaba.drop("Date", axis=1)
alibaba["Day_of_week"] = alibaba.index.day_name()
print(alibaba, end="\n\n")
print(alibaba[alibaba["Day_of_week"] == "Friday"])
