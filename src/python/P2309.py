# https://www.acmicpc.net/problem/2309
# 2024-11-25 / 2309. 일곱 난쟁이 / Bronze I

from itertools import combinations as c

H = [int(input()) for _ in range(9)]
S = sum(H)
exclude = c(range(9), 2)
for a, b in exclude:
    if S - H[a] - H[b] == 100:
        arr = [H[i] for i in range(9) if i not in (a, b)]
        arr.sort()
        print("\n".join([str(n) for n in arr]))
        break
