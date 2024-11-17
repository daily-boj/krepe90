# https://www.acmicpc.net/problem/1912
# 2024-11-18 / 1912. 연속합 / Silver II

# case 1. 연속된 양수 중 가장 긴 것
# case 2. 연속된 양수는 아닌데 그 사이에 낀 음수가 (절대값이) 작아서 붙이는게 이득인 경우

# 간단하게 생각하자
# f(n) = max(f(n-1) + n, n)

N = int(input())
A = list(map(int, input().split()))

dp = [0] * N
for i in range(N):
    dp[i] = max(dp[i - 1] + A[i], A[i])     # i == 0 일 때 dp[-1] 참조
print(max(dp))
