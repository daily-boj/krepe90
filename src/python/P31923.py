# https://www.acmicpc.net/problem/31923
# 2025-04-04 / 31923. 마라탕후루 / Bronze II

# 0..N 의 i에 대해서
# sb[i] + n*P == sm[i] + n*Q
# sb[i] - sm[i] == n * (Q - P)
# 가 성립되는 n을 구해야 함
# 단 n의 배열인 ns에 대해 sum(ns) <= 10000
# - 이거는 어차피 N, P, Q, A_i, B_i 모두 100 이하 자연수라 상관 X

N, P, Q = map(int, input().split())
sb = list(map(int, input().split()))
sm = list(map(int, input().split()))
d = P - Q

ns = []

for i in range(N):
    sb_i, sm_i = sb[i], sm[i]
    di = sb_i - sm_i
    if sb_i == sm_i:
        ns.append(0)
        continue
    if d * di > 0 or d == 0 or di % -d != 0:
        print("NO")
        break
    ns.append(di // -d)
else:
    print("YES")
    print(*ns)
