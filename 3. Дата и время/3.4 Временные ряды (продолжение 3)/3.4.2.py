from datetime import time


res = time(*(int(input()) for _ in range(3)))
print(res, type(res), sep="\n")
