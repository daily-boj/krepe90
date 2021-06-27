# https://www.acmicpc.net/problem/2232
# 2021-06-28 / 2232. 지뢰 / Silver III

# 접근방법:
# 각 지뢰는 왼쪽, 오른쪽, 혹은 양쪽에서 연쇄 반응으로 터트릴 수 있거나, 직접 터트릴 수 있다.
# 따라서 양쪽 중 어느 곳에도 자신을 터트릴 수 있는 지뢰가 없다면, 그 지뢰는 직접 터트려야 한다.
import sys
N = int(input())
M = [int(sys.stdin.readline()) for _ in range(N)]

for i, n in enumerate(M):
    pv = M[i - 1] if i > 0 else 0
    nx = M[i + 1] if i + 1 < N else 0
    if n >= pv and n >= nx:
        print(i + 1)
