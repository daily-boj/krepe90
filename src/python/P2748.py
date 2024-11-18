# https://www.acmicpc.net/problem/2748
# 2024-11-18 / 2748. 피보나치 수 2 / Bronze I

dp = [0] * 91
dp[1] = 1
for i in range(2, 91):
    dp[i] = dp[i-1] + dp[i-2]
N = int(input())
print(dp[N])
