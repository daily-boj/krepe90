# https://www.acmicpc.net/problem/2576
# 2025-03-26 / 2576. 홀수 / Bronze III
a = [int(input()) for _ in range(7)]
odd = [n for n in a if n & 1]
if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)
