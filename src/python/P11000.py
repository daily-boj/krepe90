# https://www.acmicpc.net/problem/11000
# 2024-11-19 / 11000. 강의실 배정 / Gold V


# 단순하게 생각하면 최대 N번 겹쳐지면 강의실이 N개 필요하다
# 정렬하고 아래서부터 쭉 긁으면서 겹치는거 몇개인지 스택마냥 세면 되긴 함.

import heapq
import sys
input = sys.stdin.readline

N = int(input())
ST = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
ST.sort()

hq: list[int] = []
max_stack = 0
now_stack = 0
for s, t in ST:
    heapq.heappush(hq, t)
    now_stack += 1
    while hq[0] <= s:
        heapq.heappop(hq)
        now_stack -= 1
    max_stack = max_stack if max_stack > now_stack else now_stack
print(max_stack)
