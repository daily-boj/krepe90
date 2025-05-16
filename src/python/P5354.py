# https://www.acmicpc.net/problem/5354
# 2025-05-17 / 5354. J박스 / Bronze III

T = int(input())

for _ in range(T):
    N = int(input())
    if N == 1:
        print("#")
    else:
        print("#" * N)
        for i in range(N - 2):
            print("#" + "J" * (N - 2) +  "#")
        print("#" * N)
    print()
