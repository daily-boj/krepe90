# https://www.acmicpc.net/problem/2587
# 2025-02-01 / 2587. 대표값2 / Bronze II

a = [int(input()) for _ in range(5)]
a.sort()
print(sum(a) // 5, a[2])
