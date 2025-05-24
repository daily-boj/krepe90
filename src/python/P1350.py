# https://www.acmicpc.net/problem/1350
# 2025-05-24 / 1350. 진짜 공간 / Bronze II

from math import ceil


N = int(input())
A = map(int, input().split())
S = int(input())
print(sum(ceil(a / S) * S for a in A))
