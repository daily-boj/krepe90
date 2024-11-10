# https://www.acmicpc.net/problem/2193
# 2024-11-10 / 2193. 이친수 / Silver III

# f(n) = f(n-1) + f(n-2)
N = int(input())
arr = [0, 1] + [0] * 90
for i in range(2, 91):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[N])
