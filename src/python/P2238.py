# https://www.acmicpc.net/problem/2238
# 2025-05-08 / 2238. 경매 / Silver V

import sys
input = lambda: sys.stdin.readline().rstrip()

U, N = map(int, input().split())
arr: list[list[str]] = [list() for _ in range(U + 1)]
for _ in range(N):
    S, P = input().split()
    P = int(P)
    arr[P].append(S)

rn, rp = "", 0
mn = 100000
for i, a in enumerate(arr):
    if not a:
        continue
    if len(a) < mn:
        rn = a[0]
        rp = i
        mn = len(a)
print(rn, rp)
