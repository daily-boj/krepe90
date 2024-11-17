# https://www.acmicpc.net/problem/2170
# 2024-11-18 / 2170. 선 긋기 / Gold V

# 1차원 공간에서 선을 그었을 때, 연속되는 부분을 제거하기(?)

import sys

input = sys.stdin.readline

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
A.sort(key=lambda x: x[0])

sum_length = 0
p_start, p_end = A[0]
for p1, p2 in A[1:]:
    if p1 > p_end:
        sum_length += p_end - p_start
        p_start, p_end = p1, p2
    else:
        p_end = p_end if p_end > p2 else p2
else:
    sum_length += p_end - p_start

print(sum_length)
