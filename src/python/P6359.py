# https://www.acmicpc.net/problem/6359
# 2025-01-14 / 6359. 만취한 상범 / Bronze II

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0] * 101
    for r in range(1, N + 1):
        for k in range(r, N + 1, r):
            arr[k] = arr[k] ^ 0x01
    print(sum(arr))
