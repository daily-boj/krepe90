# https://www.acmicpc.net/problem/1236
# 2020-06-12 / 1236. 성 지키기 / Bronze I
n, m = map(int, input().split(maxsplit=1))
c = 0
a = []
for i in range(n):
    a.append(input())

c = max(n - sum(1 for x in a if "X" in x), m - sum(1 for x in zip(*a) if "X" in x))

print(c)
