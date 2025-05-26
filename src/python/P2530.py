# https://www.acmicpc.net/problem/2530
# 2025-05-26 / 2530. 인공지능 시계 / Bronze IV

h, m, s = map(int, input().split())
ds = int(input())

total = (h * 60 + m) * 60 + s + ds

rd = total // 86400
rh = (total % 86400) // 3600
rm = (total % 3600) // 60
rs = total % 60

print(rh, rm, rs)
