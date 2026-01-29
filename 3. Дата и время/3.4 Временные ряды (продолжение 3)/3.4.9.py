import datetime


dt = datetime.datetime(
    int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
)
print(dt.strftime("%d %b %Y %a"))
