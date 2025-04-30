# https://www.acmicpc.net/problem/13300
# 2025-04-30 / 13300. 방 배정 / Bronze II

# 좀 더 개선을 한다면 d를 딕셔너리가 아닌 다른 자료형으로 할 수도 있지 않을까

import math

N, K = map(int, input().split())
d = {}
for _ in range(N):
    k = input()
    d[k] = d.get(k, 0) + 1
result = 0
for k, v in d.items():
    result += math.ceil(v / K)
print(result)
