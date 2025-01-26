# https://www.acmicpc.net/problem/25286
# 2025-01-26 / 25286. 11월 11일 / Bronze III

# 너무 날먹인데
from datetime import datetime as dt, timedelta as td

for _ in range(int(input())):
    y, m = map(int, input().split())
    d = dt(y, m, m) - td(days=m)
    print(d.year, d.month, d.day)
