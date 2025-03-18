# https://www.acmicpc.net/problem/5220
# 2025-03-18 / 5220. Error Detection / Bronze III

for _ in range(int(input())):
    n, c = map(int, input().split())
    cnt = sum((n >> i) & 0x01 for i in range(16))
    print("Valid" if cnt % 2 == c else "Corrupt")
