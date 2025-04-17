# https://www.acmicpc.net/problem/11328
# 2025-04-17 / 11328. Strfry / Bronze II

# 동일한 갯수의 알파벳이 쓰였는지만 확인하면 된다.

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

T = int(input())
for _ in range(T):
    ac = [0] * 26
    bc = [0] * 26
    a, b = input().split()
    for c in a:
        ac[ord(c) - 97] += 1
    for c in b:
        bc[ord(c) - 97] += 1
    print("Possible" if ac == bc else "Impossible")
