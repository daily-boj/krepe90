# https://www.acmicpc.net/problem/29722
# 2025-01-29 / 29722. 브실혜성 / Bronze III

y, m, d = map(int, input().split("-"))
N = int(input())

d, md = (d + N - 1) % 30 + 1, (d + N - 1) // 30
m, yd = (m + md - 1) % 12 + 1, (m + md - 1) // 12
y += yd

print(f"{y:04d}-{m:02d}-{d:02d}")
