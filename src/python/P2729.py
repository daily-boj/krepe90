# https://www.acmicpc.net/problem/2729
# 2025-04-23 / 2729. 이진수 덧셈 / Bronze I

T = int(input())
for _ in range(T):
    N, M = input().split()
    print(f"{int(N, 2) + int(M, 2):b}")

