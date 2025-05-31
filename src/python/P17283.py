# https://www.acmicpc.net/problem/17283
# 2025-05-31 / 17283. I am Groot / Bronze I

L = int(input())
R = int(input())
prev = int(L * R / 100)
result = 0
i = 1
while prev > 5:
    result += (2 ** i) * prev
    prev = int(prev * R / 100)
    i += 1
print(result)
