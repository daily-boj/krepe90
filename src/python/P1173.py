# https://www.acmicpc.net/problem/1173
# 2025-05-09 / 1173. 운동 / Bronze II

N, m, M, T, R = map(int, input().split())
time_left = N
time_elapse = 0
X = m

# 운동 불가능 조건
if m + T > M:
    time_left = 0
    time_elapse = -1

while time_left:
    # 운동 가능
    if X + T <= M:
        time_left -= 1
        X += T
    # 휴식 필요
    else:
        X = X - R if X - R > m else m
    time_elapse += 1
print(time_elapse)
