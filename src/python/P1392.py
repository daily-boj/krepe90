# https://www.acmicpc.net/problem/1392
# 2025-04-27 / 1392. 노래 악보 / Bronze II

# N <= 100, B_i <= 100

N, Q = map(int, input().split())
B = [int(input()) for _ in range(N)]
questions = [int(input()) for _ in range(Q)]

T = []
for i, b_i in enumerate(B):
    T += [i + 1] * b_i

print(*(T[q] for q in questions), sep="\n")
