# https://www.acmicpc.net/problem/2293
# 2024-11-22 / 2293. 동전 1 / Gold IV

# K는 1만까지인데 동전의 가치는 10만까지??

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins: list[int] = []
for _ in range(N):
    c_str = input()
    if len(c_str) > 5:
        pass
    coins.append(int(c_str))
# coins.sort()

dp = [0] * 10001
dp[0] = 1

for c in coins:
    for i in range(c, 10001):
        dp[i] = dp[i] + dp[i - c]
print(dp[K])
