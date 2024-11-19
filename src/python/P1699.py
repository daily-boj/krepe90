# https://www.acmicpc.net/problem/1699
# 2024-11-19 / 1699. 제곱수의 합 / Silver II

# f(n) = min(f(n - {1**2}), f(n - {2**2}), ...) + 1
#                                               ^^^ 이 +1은 f() 안에서 뺐던 n보다 작거나 같은 제곱수의 것
# 쨌튼 이렇게 문제 쪼개나가서 DP로 풀기

dp = [0] * 100_001
dp[0:5] = [0, 1, 2, 3, 1]
sq = [n ** 2 for n in range(1, int(100_001 ** 0.5))]
for i in range(5, 100_001):
    arr = sq[:int(i ** 0.5)]
    dp[i] = min(dp[i - n] for n in arr) + 1

print(dp[int(input())])
