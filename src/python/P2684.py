# https://www.acmicpc.net/problem/2684
# H, T로 이루어진 40자 str -> 1, 0으로 이루어진 문자열 -> int 형
# 이후 비트시프트를 통해 나오는 수(0-7)를 index처럼 사용해서 갯수를 셈
import sys
for _ in range(int(input())):
    arr: str = sys.stdin.readline()[:-1]
    res = [0, 0, 0, 0, 0, 0, 0, 0]
    i = int(arr.replace("H", "1").replace("T", "0"), 2)
    for j in range(38):
        res[i & 0b111] += 1
        i = i >> 1
    print(" ".join(map(str, res)))
