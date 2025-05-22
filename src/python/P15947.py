# https://www.acmicpc.net/problem/15947
# 2025-05-22 / 15947. 아기 석환 뚜루루 뚜루 / Bronze I

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())


arr = "baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan".split()
n = int(input()) - 1

cnt = n // len(arr)
idx = n % len(arr)
word = arr[idx]

if word == "tururu":
    if cnt > 2:
        print(f"tu+ru*{cnt+2}")
    else:
        print(word + "ru" * cnt)
elif word == "turu":
    if cnt > 3:
        print(f"tu+ru*{cnt+1}")
    else:
        print(word + "ru" * cnt)
else:
    print(word)
