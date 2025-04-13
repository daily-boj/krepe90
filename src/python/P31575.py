# https://www.acmicpc.net/problem/31575
# 2025-04-13 / 31575. 도시와 비트코인 / Silver III

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

N, M = map(int, input().split())
a = []
b = [[False] * N for _ in range(M)]
for _ in range(M):
    a.append(input().split())
b[0][0] = True
for i in range(M):
    for j in range(N):
        if a[i][j] == "0":
            b[i][j] = False
            continue
        if i > 0 and b[i - 1][j]:
            b[i][j] = True
        elif j > 0 and b[i][j - 1]:
            b[i][j] = True
print("Yes" if b[-1][-1] else "No")
