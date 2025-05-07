# https://www.acmicpc.net/problem/33810
# 2025-05-07 / 33810. SciComLove (2025) / Bronze IV

cnt = 0
for c1, c2 in zip("SciComLove", input()):
    if c1 != c2:
        cnt += 1
print(cnt)
