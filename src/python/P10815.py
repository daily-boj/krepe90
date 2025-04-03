# https://www.acmicpc.net/problem/10815
# 2025-04-03 / 10815. 숫자 카드 / Silver V
N = int(input())
nset = set(input().split())
M = int(input())
print(*(1 if n in nset else 0 for n in input().split()))
