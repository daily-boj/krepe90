# https://www.acmicpc.net/problem/2371
# 2025-04-14 / 2371. 파일 구별하기 / Silver III

# 간단하게 푸는건 그냥 해시맵 돌리는거긴 한데 100 * K 돌아서 괜찮을지 모르겠음. K 조건이 없어서...
# 튜플로 해시를 돌릴까 그냥

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

N = int(input())
arr: list[tuple[int, ...]] = []
for _ in range(N):
    arr.append(tuple(map(int, input().split()[:-1])))
K = 0
while True:
    K += 1
    s = set(a[:K] for a in arr)
    if len(arr) == len(s):
        print(K)
        break
