# https://www.acmicpc.net/problem/25643
# 2025-01-07 / 25643. 문자열 탑 쌓기 / Bronze I

# abc
#   cde
# abc
#  bcd

N, M = map(int, input().split())

s = input()
result = 1
for _ in range(N - 1):
    s_prev = s
    s = input()
    if s == s_prev:
        continue
    for i in range(1, M):
        print(f"--- {s} {s_prev} ---")
        print(s[-i:], s_prev[:i], s[:i], s_prev[-i:], sep=", ")
        if s[-i:] == s_prev[:i] or s[:i] == s_prev[-i:]:
            print("break!")
            break
    else:
        result = 0
print(result)
