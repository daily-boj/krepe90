# https://www.acmicpc.net/problem/10804
# 2024-11-26 / 10804. 카드 역배치 / Bronze II

A = list(range(1, 21))
for _ in range(10):
    s, e = map(int, input().split())
    s -= 1
    A[s:e] = A[s:e][::-1]
print(" ".join(str(n) for n in A))
