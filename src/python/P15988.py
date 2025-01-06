# https://www.acmicpc.net/problem/15988
# 2025-01-07 / 15988. 1, 2, 3 더하기 3 / Silver II

# f(1) = 1
# f(2) = 2
# 2, 1+1
# f(3) = 4
# 3, 2+1, 1+2, 1+1+1
# f(4) = f(1) + f(2) + f(3) = 7
# f(n) = f(n-3) + f(n-2) + f(n-1)

DP = [0] * 1_000_001
DP[0:4] = [0, 1, 2, 4]
for i in range(4, 1_000_001):
    DP[i] = sum(DP[i-3:i]) % 1_000_000_009

T = int(input())
for _ in range(T):
    print(DP[int(input())])
