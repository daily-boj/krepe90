# https://www.acmicpc.net/problem/14501
# 2024-11-12 / 14501. 퇴사 / Silver III

N = int(input())
T: list[int] = []
P: list[int] = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# 뒤에서부터 거꾸로 채워나가면 될 것 같음.
# f(n)이 있을 때, n + T[n] < N + 1 이라는 가정 하에
# f(n)은 max(f(n+1), P[n]+f(n+T(n)))
# 사실 N이 15라서 전부 다 해봐도 2^15니까 할만하긴 함. (약 3만번)
arr = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    if i + T[i] < N + 1:
        arr[i] = max(arr[i+1], P[i] + arr[i + T[i]])
    else:
        arr[i] = arr[i+1]
print(max(arr))
