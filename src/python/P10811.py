# https://www.acmicpc.net/problem/10811
# 2025-03-31 / 10811. 바구니 뒤집기 / Bronze II

N, M = map(int, input().split())
b = list(range(1, N + 1))
for _ in range(M):
    i, j = map(lambda n: int(n) - 1, input().split())
    b[i:j+1] = reversed(b[i:j+1])
print(*b)
