# https://www.acmicpc.net/problem/9657
# 2024-11-13 / 9657. 돌 게임 3 / Silver III

# 상근 선공, 1/3/4개
# f(1) = 상근
# f(2) = 창영
# f(3) = 상근
# f(4) = 상근
# f(5) = any of f(4) f(2) f(1) = 상근
# f(6) = any of f(5) f(3) f(2) = 상근
# f(7) = any of f(6) f(4) f(3) = 창영
SK = False
CY = True

N = int(input())
dp = [False] * (N + 1)
dp[:5] = [None, SK, CY, SK, SK]
for i in range(5, N + 1):
    dp[i] = not any((dp[i-1], dp[i-3], dp[i-4]))
print("CY" if dp[N] else "SK")
