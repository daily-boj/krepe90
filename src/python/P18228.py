# https://www.acmicpc.net/problem/18228
# 2025-05-02 / 18228. 펭귄추락대책위원회 / Bronze II

# 이터레이터 이용해서 깔끔하게 반복문을 돌면서 왼쪽 오른쪽 최소값 구해 더하기

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

N = int(input())
A = map(int, input().split())

left_min = 1_000_000_000
right_min = 1_000_000_000
for a in A:
    if a == -1:
        break
    if a < left_min:
        left_min = a
for a in A:
    if a < right_min:
        right_min = a
print(left_min + right_min)
