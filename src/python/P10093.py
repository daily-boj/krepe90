# https://www.acmicpc.net/problem/10093
# 2025-03-26 / 10093. 숫자 / Bronze II

# a, b는 두 양의 정수
# a > b, a < b, a == b

# 무작정 구현부터 하기보단 생각을 좀 하면서 코드를 짜도록 하자.

a, b = map(int, input().split())
if a == b:
    print(0)
    print()
else:
    if a > b:
        a, b = b, a
    print(b - a - 1)
    print(*range(a + 1, b))
