# https://www.acmicpc.net/problem/20360
# 2025-03-23 / 20360. Binary numbers / Bronze III
n = int(input())
print(*(i for i in range(20) if (n >> i) & 0x01))
