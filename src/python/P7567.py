# https://www.acmicpc.net/problem/7567
# 2025-06-04 / 7567. 그릇 / Bronze II

prev = ""
result = 0
for c in input():
    if prev == c:
        result += 5
    else:
        result += 10
    prev = c
print(result)
