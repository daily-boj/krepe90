# https://www.acmicpc.net/problem/1149
# 2024-11-05 / 1149. RGB거리 / Silver I

n = int(input())
_r, _g, _b = 0, 0, 0
for _ in range(n):
    s = input()
    r, g, b = map(int, s.split())
    _r, _g, _b = min((r + _g), (r + _b)), min((g + _r), (g + _b)), min((b + _r), (b + _g))
print(min(_r, _g, _b))
