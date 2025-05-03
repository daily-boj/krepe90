# https://www.acmicpc.net/problem/1463
# 2025-05-03 / 1463. 1로 만들기 / Silver III

# 이거 왜 못풀었었지
# 그냥 [0, 1, 2, 3] 채우고 4부터 시작하면 되는데

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

dp = [-1] * 1_000_001
dp[0:4] = [0, 0, 1, 1]

for i in range(4, 1_000_001):
    if i % 6 == 0:
        dp[i] = min(dp[i-1], dp[i // 2], dp[i // 3]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i-1], dp[i // 3]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i-1], dp[i // 2]) + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[int(input())])
