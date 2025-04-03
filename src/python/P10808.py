# https://www.acmicpc.net/problem/10808
# 2025-04-03 / 10808. 알파벳 개수 / Bronze IV
s = input()
print(*(s.count(c) for c in "abcdefghijklmnopqrstuvwxyz"))
