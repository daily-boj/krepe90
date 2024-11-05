# https://www.acmicpc.net/problem/3186
# 2020-06-29 / 3186. 소변기 / Silver II
K, L, N = map(int, input().split())
B = input()
y, n = 0, 0
on = False
flushed = False
for i, c in enumerate(B):
    # 순서대로 읽음
    if c == "0":
        y = 0
        n += 1
    else:
        y += 1
        n = 0

    if not on and y >= K:
        on = True

    if on and n >= L:
        on = False
        flushed = True
        print(i + 1)

if on:
    print((L - n) + i + 1)
elif not flushed:
    print("NIKAD")
