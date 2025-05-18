# https://www.acmicpc.net/problem/1568
# 2025-05-18 / 1568. 새 / Bronze II

N = int(input())
K = 1
ans = 0
while N:
    if N < K:
        K = 1
    N -= K
    ans += 1
    K += 1
print(ans)
