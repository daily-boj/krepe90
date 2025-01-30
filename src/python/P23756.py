# https://www.acmicpc.net/problem/23756
# 2025-01-30 / 23756. 노브 돌리기 / Bronze II

N = int(input())
a_0 = int(input())
d = 0
for _ in range(N):
    a_n = int(input())
    d += min((a_n - a_0) % 360, (a_0 - a_n) % 360)
    a_0 = a_n
print(d)
