# https://www.acmicpc.net/problem/3034
# 2025-01-10 / 3034. 앵그리 창영 / Bronze III
N, W, H = map(int, input().split())
mx: float = (W ** 2 + H ** 2) ** 0.5
for _ in range(N):
    print("NE" if int(input()) > mx else "DA")
