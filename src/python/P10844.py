# https://www.acmicpc.net/problem/10844
# 2024-11-13 / 10844. 쉬운 계단 수 / Silver I

# 0 1 1 1 1 1 1 1 1 1
# 1 1 2 2 2 2 2 2 2 1
# 1 3 3 4 4 4 4 4 3 2
# 대각선에 위치한 두 수의 합

dp = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
for i in range(1, int(input())):
    dp = [0] + [(dp[i-1] + dp[i+1]) % 1_000_000_000 for i in range(1, 11)] + [0]
print(sum(dp) % 1_000_000_000)
