# https://www.acmicpc.net/problem/25945
# 2025-04-16 / 25945. 컨테이너 재배치 / Silver II

# 가장 적게 옮겨야 하는 컨테이너의 갯수 m은 사실 이미 정해져있다.
# n=10, m=35면 정렬된 A 기준 앞의 다섯개는 3, 뒤의 다섯개는 4여야 한다.

import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
m = sum(a)
a.sort()

result = 0
lower = m // n
lower_i = n - m % n
for i, a_i in enumerate(a):
    if i < lower_i:
        result += abs(lower - a_i)
    else:
        result += abs(lower + 1 - a_i)
print(result // 2)
