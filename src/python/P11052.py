# https://www.acmicpc.net/problem/11052
# 2024-11-26 / 11052. 카드 구매하기 / Silver I

# 가성비가 가장 구린 카드팩을 구매하고 그걸 채우는게 주요한 부분인듯.
# 구매하고자 하는 카드 개수 n에 대해 DP[n]은 가장 비싸게 카드를 구매하는 방법
# P[i] = 구매가
# i=10일 때 P[:10] 해서 dp[10-j] 값들의 합의 최대값을 구하자
# 음 이렇게 푸는게 아닌가벼

N = int(input())
P = list(map(int, input().split()))
dp = [0] * 1001     # 1 <= N <= 1000
dp[1] = P[0]

for i in range(2, N + 1):
    dp[i] = max((dp[i-j] + P[j-1] for j in range(1, i+1)))
print(dp[N])
