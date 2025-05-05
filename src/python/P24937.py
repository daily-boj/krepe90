# https://www.acmicpc.net/problem/24937
# 2025-05-05 / 24937. SciComLove (2022) / Bronze II

N = int(input()) % 10
s = "SciComLove"
print(s[N:] + s[:N])
