# https://www.acmicpc.net/problem/20546
# 2025-04-12 / 20546. 🐜 기적의 매매법 🐜 / Silver V

# 딱히 요령은 없는 구현 문제로 보임.
# BNP: 가능한 만큼 최대한 구매
# TIMING: 3일 연속 상승/하락시 전량 판매/구매
# 비교: (현금 + 1월 14일의 주가 × 주식 수)

# 문제를 제대로 안읽었다. SAMESAME 고려 못했어...

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

m = int(input())
s = list(map(int, input().split()))

b_money, t_money = m, m
b_c, t_c = 0, 0
count = 0
prev = s[0]

for price in s:
    # bnp
    if price <= b_money:
        b_c += b_money // price
        b_money = b_money % price

    # timing
    if prev < price:
        count = max(1, count + 1)
    elif prev > price:
        count = min(-1, count - 1)
    else:
        count = 0
    prev = price
    
    if count >= 3:
        t_money += t_c * price
        t_c = 0
    if count <= -3:
        t_c += t_money // price
        t_money = t_money % price

b_total = b_money + s[-1] * b_c
t_total = t_money + s[-1] * t_c
if b_total > t_total:
    print("BNP")
elif b_total < t_total:
    print("TIMING")
else:
    print("SAMESAME")
