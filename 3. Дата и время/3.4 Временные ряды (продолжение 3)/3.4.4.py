import datetime


dt = datetime.datetime(
    int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
)
tm = dt.time()
print(tm, type(tm), sep="\n")
