# https://www.acmicpc.net/problem/13975
# 2025-05-08 / 13975. 파일 합치기 3 / Gold IV

import sys
import heapq as hq
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    K = int(input())
    q = list(map(int, input().split()))
    hq.heapify(q)

    rs = 0
    while len(q) > 1:
        a = hq.heappop(q)
        b = hq.heappop(q)
        rs = rs + a + b
        hq.heappush(q, a + b)
    print(rs)
