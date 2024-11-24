# https://www.acmicpc.net/problem/2294
# 2024-11-24 / 2294. 동전 2 / Gold V

N, K = map(int, input().split())
C: set[int] = set()
for _ in range(N):
    C.add(int(input()))

dp = [-1] * 10001
dp[0] = 0

# dp[n] : 주어진 동전들로 n원을 만들기 위한 최소 개수
# possible_coins : n원을 만들 때 쓸 수 있는 동전, 즉 n원 이하의 동전들. (n원 이상은 애초에 쓸 일이 없음)
# prev_step: dp[n-c] 결과가 -1이 아닌 값들.
#   예를 들어 동전이 2,3,5 있고 i가 10이면 prev_step은 dp[8], dp[7], dp[5] 중 -1이 아닌 (값이 있는) 값들
#   만약 i==c라면 dp[0]을 찾고, 이건 0이니까 조건이 성립해서 들어감.
for i in range(1, 10001):
    possible_coins = [c for c in C if c<=i]
    prev_step = [dp[i - c] for c in possible_coins if dp[i - c] >= 0]
    if prev_step:
        n = min(prev_step)
        dp[i] = n + 1
print(dp[K])
