# https://www.acmicpc.net/problem/1225
# 2025-03-21 / 1225. 이상한 곱셈 / Bronze II

a, b = input().split()
a, b = (a, b) if len(a) > len(b) else b, a
sa = sum(map(int, a))
print(sum(sa * n for n in map(int, b)))
