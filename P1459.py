# https://www.acmicpc.net/problem/1459
# 2020-06-29 / 1459. 걷기 / Bronze I
x, y, w, s = map(int, input().split(maxsplit=3))
if 2 * w <= s:
    # 대각선이 더 느림
    dist = (x + y) * w
elif w < s < 2 * w:
    # 대각선으로 갈 거리만 대각선으로 가는게 빠름.
    # 대각선으로 갈 거리, 직선으로 갈 거리
    diag = min(x, y)
    lin = max(x, y) - diag
    dist = diag * s + lin * w
else:
    # 가능한 모든 거리를 대각선으로
    # x + y가 홀수인 경우: 무조건 한 칸은 직선으로 가야함.
    diag = min(x, y)
    lin = max(x, y) - diag
    if lin % 2:
        diag += lin - 1
        lin = 1
    else:
        diag += lin
        lin = 0
    dist = diag * s + lin * w
print(dist)
