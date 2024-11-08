# https://www.acmicpc.net/problem/11727
# 2024-11-08 / 11727. 2×n 타일링 2 / Silver III

# f(1) = 1
# f(2) = 3
# f(3) = 5

# f(4) = 11
# f(5) = 21
# f(6) = 43
# f(7) = 85
# f(8) = 171

# f(n) = f(n-1) + 2f(n-2)
N = int(input())
if N == 1:
    print(1)
elif N == 2:
    print(3)
elif N == 3:
    print(5)
else:
    n_2, n_1, n = 3, 5, 11
    for i in range(4, N + 1):
        n = (n_1 + n_2 * 2) % 10007
        n_2, n_1 = n_1, n
    print(n)
