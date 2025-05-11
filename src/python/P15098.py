# https://www.acmicpc.net/problem/15098
# 2025-05-11 / 15098. No Duplicates / Bronze I

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

s = input().split()
cnt = {}
for w in s:
    cnt[w] = cnt.get(w, -1) + 1
print("no" if any(cnt.values()) else "yes")
