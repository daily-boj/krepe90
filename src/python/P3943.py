# https://www.acmicpc.net/problem/3943
# 2025-01-08 / 3943. 헤일스톤 수열 / Bronze II

# 4, 2, 1, 4, 2, 1, ...
# 1이 되면 수열 끝.
# 50의 최대값은 50 25 76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 4 2 1 -> 88

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    mx = n
    while n != 1:
        n = n * 3 + 1 if n & 0x01 else n >> 1
        mx = max(n, mx)
    print(mx)
