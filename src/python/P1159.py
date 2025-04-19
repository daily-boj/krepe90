# https://www.acmicpc.net/problem/1159
# 2025-04-19 / 1159. 농구 경기 / Bronze II

# 각 줄 입력의 첫 글자를 알파벳으로 입력받아서 갯수 세고, 5개 이상이면 OK

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

N = int(input())
a = [0] * 26
for _ in range(N):
    a[ord(input()[0]) - 97] += 1
result = "".join(chr(i + 97) for i in range(26) if a[i] >= 5)
print(result if result else "PREDAJA")
