# https://www.acmicpc.net/problem/1965
# 2024-11-25 / 1965. 상자넣기 / Silver II

N = int(input())
BOXES = map(int, input().split())

dp = [0] * 1001
for b in BOXES:
    dp[b] = max(dp[:b]) + 1
print(max(dp))
