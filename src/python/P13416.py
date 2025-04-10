# https://www.acmicpc.net/problem/13416
# 2025-04-10 / 13416. 주식 투자 / Bronze III

# 각 일자별로 max(A, B, C, 0)을 구해 모두 더하면 된다.

import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    print(str(sum([
        max(*map(int, input().split()), 0)
        for _ in range(N)
    ])))
