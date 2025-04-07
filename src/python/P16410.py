# https://www.acmicpc.net/problem/16410
# 2025-04-07 / 16410. Goat Rope / Bronze I

# (x, y)에 기둥(점) -> p
# (x1, y1, x2, y2)에 집 (직사각형)
# 기둥에서 집까지의 최소 거리를 출력
# 직사각형의 각 꼭짓점을 a,b,c,d라고 하고, p랑 가장 가까운 지점이 있는 변이 대충 ab라고 가정
# 그러면 삼각형 pab의 (ab를 밑변으로 한) 높이가 최소거리가 됨.
# 근데 직·둔각삼각형이면 pa가 최단거리니까 대충 pa~pd까지도 각각 구해서 최소값 구하기.


def d(n):
    x, y, dx, dy = n
    return ((dx - x) ** 2 + (dy - y) ** 2) ** 0.5


x, y, x1, y1, x2, y2 = map(int, input().split())

if x1 <= x <= x2:
    print(min(abs(y1 - y), abs(y2 - y)))
elif y1 <= y <= y2:
    print(min(abs(x1 - x), abs(x - x2)))
else:
    print(min(map(d, [(x, y, x1, y1), (x, y, x1, y2), (x, y, x2, y1), (x, y, x2, y2)])))
