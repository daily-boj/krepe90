# https://www.acmicpc.net/problem/2302
# 2024-11-14 / 2302. 극장 좌석 / Silver I

# 연속된 일반 좌석의 길이별 가능한 수를 전부 곱해주면 됨.
# f(1) = 1
# f(2) = 2
# f(3) = 3
# f(4) = 5
# f(5) = 8

dp = [0, 1, 2] + [0] * 38
for i in range(3, 41):
    dp[i] = dp[i - 1] + dp[i - 2]

N = int(input())
M = int(input())

lock_list = [0] + [int(input()) for _ in range(M)] + [N + 1]
arr = [n - m - 1 for n, m in zip(lock_list[1:], lock_list) if n - m - 1]

result = 1
for a in arr:
    result *= dp[a]
print(result)
