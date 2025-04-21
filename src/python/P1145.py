# https://www.acmicpc.net/problem/1145
# 2025-04-21 / 1145. 적어도 대부분의 배수 / Bronze I

# 세 수의 최소공배수를 구하고, 그 중 최소를 출력


from itertools import combinations
from math import gcd

A = list(map(int, input().split()))
rs = set()
for a, b, c in combinations(A, 3):
    ab = a * b // gcd(a, b)
    abc = ab * c // gcd(ab, c)
    rs.add(abc)
print(min(rs))
