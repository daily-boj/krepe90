# https://www.acmicpc.net/problem/15565
# 2020-06-30 / 15565. 귀여운 라이언 / Silver I


# 시간 초과로 아래 코드는 버릴 예정.
# import sys
# N, K = map(int, sys.stdin.readline().split())
# D = sys.stdin.readline().split()
# m = 100001
# for i in range(N - K + 1):
#     if D[i] != "1":
#         continue
#     cnt = 0
#     for j in range(i, min(N, i + m)):
#         if D[j] == "1":
#             cnt += 1
#         else:
#             continue
#         if cnt >= K:
#             if j - i + 1 < m:
#                 m = j - i + 1
#             break
# print(m if m < 100001 else -1)


import sys
N, K = map(int, sys.stdin.readline().split())
D = sys.stdin.readline().split()
x = []
cnt = 0
# O(N)
for c in D:
    if c == "1":
        x.append(cnt)
        cnt = 0
    else:
        cnt += 1
if len(x) < K:
    print(-1)
elif len(x) == K:
    print(K)
else:
    x.pop(0)
    r = K - 1
    sum_list = [sum(x[: r])]
    for i in range(1, len(x) - K + 2):
        sum_list.append(sum_list[-1] - x[i - 1] + x[i + r - 1])
    print(min(sum_list) + K)
