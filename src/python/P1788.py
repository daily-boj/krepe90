# https://www.acmicpc.net/problem/1788
# 2024-11-14 / 1788. 피보나치 수의 확장 / Silver III

# f(n) = f(n-1) + f(n-2)
# f(n-2) = f(n) - f(n-1)

# dp[-1_000_000] = dp[1_000_001]
dp = [0] * 2_000_001
# 양수
dp[1] = 1
for i in range(2, 1_000_001):
    dp[i] = (dp[i-1] + dp[i-2]) % 1_000_000_000
# 음수
for i in range(-1, -1_000_001, -1):
    n = dp[i+2] - dp[i+1]
    if n < 0:
        dp[i] = -((-n) % 1_000_000_000)
    else:
        dp[i] = n % 1_000_000_000
# 결과
N = int(input())
result = dp[N]
if result == 0:
    print(0)
elif result > 0:
    print(1)
else:
    print(-1)
print(abs(result))
