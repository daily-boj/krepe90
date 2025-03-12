# https://www.acmicpc.net/problem/25183
# 2025-03-12 / 25183. 인생은 한 방 / Bronze I

N = int(input())
S = map(ord, input())

prev, cnt = 0, 0
for i, c in enumerate(S):
    if c - 1 == prev or c + 1 == prev:
        cnt += 1
    else:
        cnt = 0

    if cnt >= 4:
        break
    prev = c
print("YES" if cnt >= 4 else "NO")
