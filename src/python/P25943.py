# https://www.acmicpc.net/problem/25943
# 2024-11-20 / 25943. 양팔저울 / Silver IV

N = int(input())
A = list(map(int, input().split()))

L, R = 0, 0
for a in A:
    if L <= R:
        L += a
    else:
        R += a

diff = abs(L - R)
w_cnt = 0
for w in (100, 50, 20, 10, 5, 2, 1):
    w_cnt += diff // w
    diff = diff % w
print(w_cnt)
