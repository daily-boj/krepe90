# https://www.acmicpc.net/problem/29716
# 2025-04-14 / 29716. 풀만한문제 / Bronze II

# 실수를 좀 많이 했다. isupper 말고 upper를 썼다던지, 4를 더해야 하는데 2를 더했다던지...

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write


def score(s: str):
    sc = 0
    for c in s:
        if c.isupper():
            sc += 4
        elif c.islower() or c.isdigit():
            sc += 2
        else:
            sc += 1
    return sc

J, N = map(int, input().split())

result = 0
for _ in range(N):
    if score(input()) <= J:
        result += 1
print(result)
