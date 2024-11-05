# https://www.acmicpc.net/problem/14400
# 2020-07-10 / 14400. 편의점 2 / Silver II
import sys
T = int(input())
arr_x, arr_y = [], []
for _ in range(T):
    X, Y = map(int, sys.stdin.readline().rstrip().split())
    arr_x.append(X)
    arr_y.append(Y)
med_x, med_y = sorted(arr_x)[len(arr_x) // 2], sorted(arr_y)[len(arr_y) // 2]
print(sum(abs(n - med_x) for n in arr_x) + sum(abs(n - med_y) for n in arr_y))
