# https://www.acmicpc.net/problem/2154
# 2025-06-02 / 2154. 수 이어 쓰기 3 / Bronze II

print("".join(str(n) for n in range(1, 100_001)).find(input()) + 1)
