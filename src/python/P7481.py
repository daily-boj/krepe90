# https://www.acmicpc.net/problem/7481
# 2020-07-10 / 7481. ATM놀이 / Bronze I
T = int(input())
for _ in range(T):
    A, B, S = map(int, input().split())
    swap = False
    if A > B:
        swap = True
        A, B = B, A
    for j in range(S // B, -1, -1):
        if (S - (B * j)) % A == 0:
            i = (S - (B * j)) // A
            if swap:
                print(j, i)
            else:
                print(i, j)
            break
    else:
        print("Impossible")
