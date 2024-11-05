# https://www.acmicpc.net/problem/3062
# 2020-06-11 / 3062. 수 뒤집기 / Bronze II
for _ in range(int(input())):
    x = input()
    y = int(x) + int(x[::-1])
    if str(y) == str(y)[::-1]:
        print("YES")
    else:
        print("NO")
