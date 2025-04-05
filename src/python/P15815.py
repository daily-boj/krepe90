# https://www.acmicpc.net/problem/15815
# 2025-04-05 / 15815. 천재 수학자 성필 / Silver III

# 후위 표기식 순한맛
# 빼기, 나누기는 순서에 유의할 것...

m = {
    "+": int.__add__,
    "-": int.__rsub__,
    "*": int.__mul__,
    "/": int.__rfloordiv__
}
s = []
for c in input():
    if c.isdigit():
        s.append(int(c))
    else:
        s.append(m[c](s.pop(), s.pop()))
print(s[-1])
