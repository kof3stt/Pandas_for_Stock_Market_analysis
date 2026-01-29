import datetime


dt = datetime.datetime(
    int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
)
print(dt + datetime.timedelta(days=150, hours=12))
