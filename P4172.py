# https://www.acmicpc.net/problem/4172
# 2021-06-29 / 4172. sqrt log sin / Silver I

import math


def sqrt(n):
    return math.floor(n - math.sqrt(n))


def log(n):
    return math.floor(math.log(n))


def sin(n):
    return math.floor(n * math.sin(n) * math.sin(n))


A = [0] * 1000001
A[0] = 1
for i in range(1, 1000001):
    A[i] = (A[sqrt(i)] + A[log(i)] + A[sin(i)]) % 1000000

while True:
    v = int(input())
    if v == -1:
        break
    print(A[v])
