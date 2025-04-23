# https://www.acmicpc.net/problem/15873
# 2025-04-24 / 15873. 공백 없는 A+B / Bronze IV

S = input()
if S[:2] == "10":
    print(int(S[:2]) + int(S[2:]))
else:
    print(int(S[0]) + int(S[1:]))
