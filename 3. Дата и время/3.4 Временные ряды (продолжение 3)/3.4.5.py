import datetime


dt = datetime.datetime(
    int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
)
date = dt.date()
print(date, type(date), sep="\n")
