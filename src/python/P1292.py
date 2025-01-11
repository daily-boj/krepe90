# https://www.acmicpc.net/problem/1292
# 2025-01-12 / 1292. 쉽게 푸는 문제 / Bronze I


def arr():
    yield 0
    for i in range(50):
        for j in range(i):
            yield i

N, M = map(int, input().split())
print(sum([n for n in arr()][N:M+1]))
