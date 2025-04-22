# https://www.acmicpc.net/problem/2501
# 2025-04-22 / 2501. 약수 구하기 / Bronze III

# 그냥 브루트포스 문제

N, K = map(int, input().split())
idx = 0
for n in range(1, N+1):
    if N % n == 0:
        idx += 1
    if K == idx:
        print(n)
        break
else:
    print(0)
