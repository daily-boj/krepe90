# https://www.acmicpc.net/problem/7489
# 2025-05-27 / 7489. 팩토리얼 / Bronze II

arr = [0] * 1001
arr[0] = 1
for i in range(1, 1001):
    r = arr[i-1] * i
    while r % 10 == 0:
        r //= 10
    arr[i] = r % 1000

for _ in range(int(input())):
    print(arr[int(input())] % 10)
