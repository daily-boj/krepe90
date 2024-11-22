# https://www.acmicpc.net/problem/11055
# 2024-11-22 / 11055. 가장 큰 증가하는 부분 수열 / Silver II

N = int(input())
A = list(map(int, input().split()))

dp = [0] * 1001     # 0 <= i <= 999
for a in A:
    dp[a] = max(dp[:a]) + a
print(max(dp))
