# https://www.acmicpc.net/problem/9358
# 2025-04-06 / 9358. 순열 접기 게임 / Silver V

from math import ceil


for i in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))

    while len(a) > 2:
        N = ceil(N / 2)
        for j in range(N):
            a[j] += a[-j-1]
        a = a[:N]
    print("Case #{}: {}".format(i + 1, "Alice" if a[0] > a[1] else "Bob"))
