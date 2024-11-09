# https://www.acmicpc.net/problem/2847
# 2024-11-09 / 2847. 게임을 만든 동준이 / Silver IV
N = int(input())
S = [int(input()) for _ in range(N)]

prev = S[-1]
result = 0
for n in S[-2::-1]:
    if prev <= n:
        result = result + (n - prev + 1)
        prev = prev - 1
    else:
        prev = n
print(result)
