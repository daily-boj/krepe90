# https://www.acmicpc.net/problem/1541
# 2024-11-24 / 1541. 잃어버린 괄호 / Silver II

# 귀찮으니 대충 깨자
# - 뒤에 있으면 싹 다 괄호로 묶어서 +를 -로 만들어버릴 수 있다.

S = input()

tmp: list[str] = []
minus = False
result = 0
for s in S:
    if s in ("+", "-"):
        n = int("".join(tmp))
        tmp = []
        if minus:
            result -= n
        else:
            result += n
        minus = (minus or s == "-")
    else:
        tmp.append(s)
else:
    n = int("".join(tmp))
    if minus:
        result -= n
    else:
        result += n
print(result)
