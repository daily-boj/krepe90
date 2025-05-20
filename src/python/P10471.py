# https://www.acmicpc.net/problem/10471
# 2025-05-20 / 10471. 공간을 만들어 봅시다 / Bronze II

# 0에서 P1, P2, ..., Pn, W까지의 거리
# P1에서 P2, ... Pn, W까지의 거리

W, P = map(int, input().split())
A = list((0, *map(int, input().split()), W))

s = set()
for i in range(P + 2):
    for j in range(i + 1, P + 2):
        s.add(A[j] - A[i])
print(*sorted(s))
