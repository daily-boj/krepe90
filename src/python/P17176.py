# https://www.acmicpc.net/problem/17176
# 2025-05-28 / 17176. 암호해독기 / Bronze I

_ = int(input())
A = map(int, input().split())
S = input()
char_map = {c: i for i, c in enumerate(" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")}
cnt_1 = [0] * 53
cnt_2 = [0] * 53
for i in A:
    cnt_1[i] += 1
for c in S:
    cnt_2[char_map[c]] += 1
print("y" if cnt_1 == cnt_2 else "n")
