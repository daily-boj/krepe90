# https://www.acmicpc.net/problem/2446
# 2025-03-20 / 2446. 별 찍기 - 9 / Bronze III

n = int(input())
r = [
    ' ' * (n - i - 1) + '*' * (2 * i + 1)
    for i in range(n)
]
print(*r[:0:-1], *r, sep="\n")
