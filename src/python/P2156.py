# https://www.acmicpc.net/problem/2156
# 2024-11-18 / 2156. 포도주 시식 / Silver I

# 포도주 잔의 개수 n
# 6, 10, 13, 9, 8, 1
# f(1) = 6  (01)
# f(2) = 16 (11)
# f(3) = 33 (011) / 19 (101) / 16 (110)
#       f(i-3) + N[i-1] + N[i]
#       f(i-2) + N[i]
#       f(i-1)

import sys


input = sys.stdin.readline
N = int(input().rstrip())
A = [int(input().rstrip()) for _ in range(N)]

dp = [0] * (N)
dp[0] = A[0]
if N > 1:
    dp[1] = A[0] + A[1]
for i in range(2, N):
    dp[i] = max(
        dp[i-3] + A[i-1] + A[i],
        dp[i-2] + A[i],
        dp[i-1],
    )
print(dp[-1])
