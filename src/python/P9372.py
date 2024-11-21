# https://www.acmicpc.net/problem/9372
# 2024-11-22 / 9372. 상근이의 여행 / Silver IV

# 상근이가 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수를 출력한다.
# 타게 되는 비행기 종류(항공노선)의 최소 = N-1개
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    for __ in range(M):
        input()
    print(N-1)
