# https://www.acmicpc.net/problem/16130
# 2025-05-10 / 16130. 벌점 (DemeritPoints) / Bronze I

# 전후 계산하는데, 벌점 // 10이 증가했으면 결과값에 +1

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

T = int(input())

for _ in range(T):
    s = input()
    point = 0
    week = 0
    for c in s:
        cn = ord(c)
        if 48 <= cn <= 57:
            cn -= 48
        else:
            cn -= 55

        if (point + cn) >= 50:
            print(f"{week}(09)")
            break
        elif (point + cn) >= 40:
            print(f"{week}(weapon)")
            break
        elif (point + cn) // 10 != point // 10:
            week += (point + cn) // 10
            point += cn
        else:
            point += cn
    else:
        print(week)
