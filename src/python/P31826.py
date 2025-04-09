# https://www.acmicpc.net/problem/31826
# 2025-04-09 / 31826. 주식 시장 / Silver III

# 현재 가격: 마지막 거래 가격
# 거래: 특정 호가의 주문의 개수의 절대값이 줄어드는 경우(?)
#      부호가 다른지 확인하는 식으로 구현.

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

s: dict[int, int] = {}
current_p = 10000
for _ in range(N):
    p, _x, f = map(int, input().split())
    x = _x * f
    current_s = s.get(p, 0)
    if current_s * x < 0:
        current_p = p
    s[p] = s.get(p, 0) + x

print(current_p)
