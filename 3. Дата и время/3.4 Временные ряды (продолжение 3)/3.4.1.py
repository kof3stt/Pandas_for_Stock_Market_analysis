from datetime import date


day, month, year = [int(input()) for _ in range(3)]
dt = date(year, month, day)
print(dt, type(dt), sep="\n")
