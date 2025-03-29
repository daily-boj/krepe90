# https://www.acmicpc.net/problem/2628
# 2025-03-29 / 2628. 종이자르기 / Silver V

# 가로세로 각각 잘린 지점 -> 잘린 길이를 구한 다음, 최대 길이를 구하고 곱하기

w, h = map(int, input().split())
r, c = [0], [0]
for i in range(int(input())):
    t, p = map(int, input().split())
    if t == 0:
        r.append(p)
    else:
        c.append(p)
r.sort()
c.sort()
r.append(h)
c.append(w)
wm = max(map(lambda x: x[1] - x[0], zip(c[:-1], c[1:])))
hm = max(map(lambda x: x[1] - x[0], zip(r[:-1], r[1:])))
print(wm * hm)
