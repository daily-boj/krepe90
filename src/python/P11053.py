# https://www.acmicpc.net/problem/11053
# 2024-11-10 / 11053. 가장 긴 증가하는 부분 수열 / Silver II

# 1 <= N <= 1000
# 1 <= A <= 1000
# A[i] 이전까지 A[i]보다 작은 부분수열의 합(?)을 찾아서 그 중 max() 한 값이 i에서의 A[i] 값의 부분수열의 합
N = int(input())
A = list(map(int, input().split()))
dp = [0] * 1001     # 1 <= i <= 1001

for a in A:
    dp[a] = max(dp[:a]) + 1
print(dp[:10])
print(max(dp))
