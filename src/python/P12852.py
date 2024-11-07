# https://www.acmicpc.net/problem/12852
# 2024-11-07 / 12852. 1로 만들기 2 / Silver I
N = int(input())
arr = [0] * (N + 1)

# 1. DP
for i in range(2, N + 1):
    if i % 6 == 0:
        arr[i] = min(arr[i // 3], arr[i // 2], arr[i - 1]) + 1
    elif i % 3 == 0:
        arr[i] = min(arr[i // 3], arr[i - 1]) + 1
    elif i % 2 == 0:
        arr[i] = min(arr[i // 2], arr[i - 1]) + 1
    else:
        arr[i] = arr[i - 1] + 1

# 2. Solve
n = N
print(arr[n])
while n > 1:
    print(n, end=" ")
    if n % 3 == 0 and arr[n // 3] == arr[n] - 1:
        n = n // 3
    elif n % 2 == 0 and arr[n // 2] == arr[n] - 1:
        n = n // 2
    else:
        n = n - 1
print(n)
