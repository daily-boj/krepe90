# https://www.acmicpc.net/problem/10708
# 2025-05-19 / 10708. 크리스마스 파티 / Bronze II

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
A = map(int, input().split())

scores = [0] * (N + 1)
for target_ans in A:
    B = map(int, input().split())
    wrong = 0
    for j, target in enumerate(B, 1):
        if target_ans == target:
            scores[j] += 1
        else:
            wrong += 1
    scores[target_ans] += wrong
print(*scores[1:], sep="\n")
