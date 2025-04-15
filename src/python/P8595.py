# https://www.acmicpc.net/problem/8595
# 2025-04-16 / 8595. 히든 넘버 / Bronze I

# 연속된 숫자만 찾아서 뽑아내야 한다.

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

N = int(input())
stack = []
result = 0
for c in input():
    if c.isdigit():
        stack.append(c)
    elif stack:
        result += int("".join(stack))
        stack.clear()
    else:
        stack.clear()
        continue
if stack:
    result += int("".join(stack))
print(result)
