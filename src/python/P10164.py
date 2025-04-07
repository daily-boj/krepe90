# https://www.acmicpc.net/problem/10164
# 2025-04-07 / 10164. 격자상의 경로 / Silver II

# 동그라미가 없다 -> 전부 다
# 동그라미가 있다 -> 동그라미 기준으로 좌상/우하 쪼개서 곱하기
# 구하는건 어떻게 -> DP
# 동그라미의 위치는 어떻게 -> dp에서 쓰던 방식 반대로 나누기/나머지 값 사용

def dp(n, m):
    arr = [0] * n * m
    arr[0] = 1
    for i in range(n):
        for j in range(m):
            pos = i * m + j
            if i > 0:
                arr[pos] += arr[(i - 1) * m + j]
            if j > 0:
                arr[pos] += arr[i * m + j - 1]
    return arr[-1]
            


N, M, K = map(int, input().split())
if K:
    n, m = (K - 1) // M, (K - 1) % M
    print(dp(n + 1, m + 1) * dp(N-n, M-m))
else:
    print(dp(N, M))
