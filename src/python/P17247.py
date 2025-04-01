# https://www.acmicpc.net/problem/17247
# 2025-04-01 / 17247. 택시 거리 / Bronze I

# 택시거리 = 맨허튼 거리
# "1"이 위치한 좌표의 거리차이

from itertools import product

N, M = map(int, input().split())
a = [input().split() for _ in range(N)]

p = []
for (y, x) in product(range(N), range(M)):
    if a[y][x] == "1":
        p.append((y, x))
print(abs(p[1][0] - p[0][0]) + abs(p[1][1] - p[0][1]))
