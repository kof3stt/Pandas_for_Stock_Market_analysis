import datetime


dt = datetime.datetime(
    int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
)
print(dt.day, dt.month, dt.year, sep="\n")
