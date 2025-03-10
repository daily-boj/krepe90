# https://www.acmicpc.net/problem/30804
# 2025-03-10 / 30804. 과일 탕후루 / Silver II

# 탕 탕 후루후루 탕탕 후루루루루
# 두 포인터 문제같은데

N = int(input())
S = list(map(int, input().split()))
s, e = 0, 0
f = {n: 0 for n in range(10)}
mx = 0
while s < N:
    if sum(1 for n in f.values() if n) > 2:
        f[S[s]] -= 1
        s += 1
    elif e >= N:
        mx = max(e - s, mx)
        break
    else:
        mx = max(e - s, mx)
        f[S[e]] += 1
        e += 1
print(mx)
