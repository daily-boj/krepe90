# https://www.acmicpc.net/problem/28097
# 2025-05-25 / 28097. 모범생 포닉스 / Bronze IV

N = int(input())
h = sum(map(int, input().split())) +  8 * (N - 1)
print(h // 24, h % 24)
