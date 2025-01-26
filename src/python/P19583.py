# https://www.acmicpc.net/problem/19583
# 2025-01-26 / 19583. 싸이버개강총회 / Silver II

import sys

input = lambda: sys.stdin.readline().rstrip()


S, E, Q = input().split()
i, o = set(), set()
while True:
    try:
        ts, name = input().split()
        if ts <= S:
            i.add(name)
        if E <= ts <= Q:
            o.add(name)
    except:
        break
print(len(i & o))
