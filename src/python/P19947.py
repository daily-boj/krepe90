# https://www.acmicpc.net/problem/19947
# 2025-04-09 / 19947. 투자의 귀재 배주형 / Silver V

# 5년 -> 3년 -> 1년
# 라고만 생각했는데, 다시 생각해보니 순서 때문에 DP를 사용해야 함.
# 항상 소수점 버림 연산 수행하기

H, Y = map(int, input().split())

dp = [H] + [0] * Y
for i in range(1, Y + 1):
    if i >= 5:
        dp[i] = max(
            int(dp[i - 5] * 1.35),
            int(dp[i - 3] * 1.20),
            int(dp[i - 1] * 1.05),
        )
    elif i >= 3:
        dp[i] = max(
            int(dp[i - 3] * 1.20),
            int(dp[i - 1] * 1.05),
        )
    else:
        dp[i] = int(dp[i - 1] * 1.05)
print(dp[-1])
