# https://www.acmicpc.net/problem/15486
# 2024-11-12 / 15486. 퇴사 2 / Gold V

# src/python/P14501.py 파일과 같은 문제
# 인데 N이 최대 1500000인
# 입력 횟수가 많아서 정리를 좀 해야 함.

# 식 자체는 동일하게
# f(n)이 있을 때, n + T[n] < N + 1 이라는 가정 하에
# f(n)은 max(f(n+1), P[n]+f(n+T(n)))
# 추가로 입출력이 느린거같아서 손을 좀 봤다

import sys

input = sys.stdin.readline

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]

arr = [0] * (N + 51)
for i in range(N - 1, -1, -1):
    T, P = A[i]
    Ti = T + i
    arr[i] = max(arr[i + 1], P + arr[Ti])
    # arr[i] = arr[i+1]
    # if i + A[i][0] < N + 1 and A[i][1] + arr[i + A[i][0]] > arr[i]:
    #     arr[i] = A[i][1] + arr[i + A[i][0]]
print(arr[0])
