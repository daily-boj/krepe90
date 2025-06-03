# https://www.acmicpc.net/problem/23321
# 2025-06-03 / 23321. 홍익 댄스파티 / Bronze I

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

"""
도약 준비 	도약 중 	착석
1 	. 	o 	.
2 	o 	w 	.
3 	m 	l 	o
4 	l 	n 	L
5 	n 	. 	n
"""

form = ["..oLn", ".omln", "owln."]
S = [input() for _ in range(5)]
ty = [{"o": 2, "w": 1, ".": 0}[c] for c in S[1]]
for i in range(5):
    print("".join(form[t][i] for t in ty))
