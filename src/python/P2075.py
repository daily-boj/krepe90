# https://www.acmicpc.net/problem/2075
# 2025-05-01 / 2075. N번째 큰 수 / Silver III

# 당연히 heapq를 쓰면 되는데 수가 너무 큰게 이슈
# 매 횟수마다 nlargest를 구하고 merge 하면 되나...?
# 되게 비효율적인데...

import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
hq = []
for _ in range(N):
    hq.extend([n for n in map(int, input().split())])
    hq = heapq.nlargest(N, hq)
print(hq[-1])
