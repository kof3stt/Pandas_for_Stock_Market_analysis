from datetime import datetime


day, month, year, hour, minute, second = [int(input()) for _ in range(6)]
dt = datetime(year, month, day, hour, minute, second)
print(dt, type(dt), sep="\n")
