# https://www.acmicpc.net/problem/1915
# 2024-11-20 / 1915. 가장 큰 정사각형 / Gold IV

# N이 세로길이, M이 가로길이

def pprint(arr: list[list[int]]):
    for sub_arr in arr:
        print(" ".join(str(n) for n in sub_arr))

N, M = map(int, input().split())
A: list[list[int]] = []
for _ in range(N):
    A.append(list(map(int, input())))

dp = [[0] * (M + 1) for _ in range(N + 1)]
for n in range(N - 1, -1, -1):
    for m in range(M - 1, -1, -1):
        if A[n][m]:
            dp[n][m] = min(dp[n+1][m], dp[n][m+1], dp[n+1][m+1]) + 1
print(max(max(arr) for arr in dp) ** 2)
