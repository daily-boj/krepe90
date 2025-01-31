# https://www.acmicpc.net/problem/25400
# 2025-01-31 / 25400. 제자리 / Bronze I
N = int(input())
A = list(map(int, input().split()))

n = 1
for a in A:
    if a == n:
        n += 1
print(N - n + 1)
