# https://www.acmicpc.net/problem/2033
# 2020-07-07 / 2033. 반올림 / Bronze I

N = int(input())
x = 0
while True:
    if N > pow(10, x + 1):
        y = N % pow(10, x + 1)
        if y < 5 * (10 ** x):
            N -= y
        else:
            N += (pow(10, x + 1) - y)   
    else:
        break
    x += 1
print(N)
