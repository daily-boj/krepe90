# https://www.acmicpc.net/problem/1081
# 2020-06-12 / 1081. 합 / Gold III


def sumd(x):
    return sum(map(int, str(x)))


def D(x):
    sumexp = [0, 45, 900, 13500, 180000, 2250000, 27000000, 315000000, 3600000000, 40500000000]
    n = 1
    res = 0
    res += sum(sumd(i) for i in range(x - (x % 10), x + 1))
    x -= x % 10
    while (0 < x):
        while x % pow(10, n + 1) > 0:
            x -= pow(10, n)
            res += sumd(x) * pow(10, n) + sumexp[n]
        n += 1
    return res


low, up = map(int, input().split(maxsplit=1))
if up == low:
    print(sumd(up))
else:
    print(D(up) - D(low - 1 if low > 0 else 0))
