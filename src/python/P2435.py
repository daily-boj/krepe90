# https://www.acmicpc.net/problem/2435
# 2025-05-06 / 2435. 기상청 인턴 신현수 / Bronze I

N, K = map(int, input().split())
A = list(map(int, input().split()))

print(max(sum(A[i: i + K]) for i in range(N - K + 1)))
