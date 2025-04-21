# https://www.acmicpc.net/problem/1992
# 2025-04-21 / 1992. 쿼드트리 / Silver I

# 단순한 분할정복 문제
# 주의해야 했던 부분: a==b==c==d 인데, 이 때 a = "(0011)" 뭐 이런 값이면 압축해선 안된다.
# 따라서 a의 길이는 1이여야 함. (다른 조건도 가능)

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write


def f(arr: list[str], x, y, n) -> str:
    if n == 1:
        return arr[y][x]
    n2 = n // 2
    x2, y2 = x + n2, y + n2
    a = f(arr, x, y, n2)
    b = f(arr, x2, y, n2)
    c = f(arr, x, y2, n2)
    d = f(arr, x2, y2, n2)
    if a == b == c == d and len(a) == 1:
        return a
    else:
        return f"({a}{b}{c}{d})"


N = int(input())
arr = []
for _ in range(N):
    arr.append(input())
print(f(arr, 0, 0, N))
