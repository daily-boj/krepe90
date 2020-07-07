# https://www.acmicpc.net/problem/3372
# 2020-07-07 / 3372. 보드 점프 / Silver I
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
B = [[0] * N for n in range(N)]
B[0][0] = 1

for i, y in enumerate(A):
    for j, x in enumerate(y):
        if x > 0:
            if j + x < N:
                B[i][j + x] += B[i][j]
            if i + x < N:
                B[i + x][j] += B[i][j]
        else:

            pass

print(B[-1][-1])
