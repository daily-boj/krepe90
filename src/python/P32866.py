# https://www.acmicpc.net/problem/32866
# 2025-04-13 / 32866. 코인의 신 건모 / Bronze III

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

N = int(input())
X = int(input()) / 100

print((N / (N * (1-X)) - 1) * 100)
