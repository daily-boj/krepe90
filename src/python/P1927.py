# https://www.acmicpc.net/problem/1927
# 2025-01-08 / 1927. 최소 힙 / Silver II

import sys
import heapq
input = sys.stdin.readline

hq = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(hq, x)
    elif hq:
        print(heapq.heappop(hq))
    else:
        print(0)
