# https://www.acmicpc.net/problem/31628
# 2025-01-29 / 31628. 가지 한 두름 주세요 / Bronze III

gaji = [input().split() for _ in range(10)]

for i in range(10):
    if len(set(gaji[i])) == 1:
        print(1)
        break
    if len(set(gaji[j][i] for j in range(10))) == 1:
        print(1)
        break
else:
    print(0)
