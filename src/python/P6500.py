# https://www.acmicpc.net/problem/6500
# 2025-03-19 / 6500. 랜덤 숫자 만들기 / Bronze II

while (a0 := int(input())):
    s = set((a0, ))
    ai = a0
    while ai:
        ai = ai ** 2 // 100 % 10000
        if ai in s:
            break
        s.add(ai)
    print(len(s))
