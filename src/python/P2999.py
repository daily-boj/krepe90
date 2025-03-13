# https://www.acmicpc.net/problem/2999
# 2025-03-13 / 2999. 비밀 이메일 / Bronze I

# 행렬의 전치(T)
# import numpy as np
# # 하고싶다

from itertools import product

msg = input()
N = len(msg)
R, C = 0, 0
for i in range(int(N ** 0.5), 0, -1):   # 이
    if N % i == 0:
        R, C = i, N // i
        break
print("".join(msg[j * R + i] for i, j in product(range(R), range(C))))
