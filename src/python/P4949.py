# https://www.acmicpc.net/problem/4949
# 2025-01-13 / 4949. 균형잡힌 세상 / Silver IV

# 간단한 스택(?)문제같은데

while True:
    S = input()
    if S == ".":
        break

    s = []
    for c in S:
        if c in "[()]":
            if c in "([":
                s.append(c)
            elif not s:
                s.append("_")
            elif (s[-1] == "[" and c == "]") or (s[-1] == "(" and c == ")"):
                s.pop()
            else:
                s.append("_")
    else:
        print("yes" if not s else "no")
