# https://www.acmicpc.net/problem/2386
# 2025-05-15 / 2386. 도비의 영어 공부 / Bronze II

while True:
    s = input()
    if s == "#":
        break

    c = s[0]
    print(c, s[2:].lower().count(c))
