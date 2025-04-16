# https://www.acmicpc.net/problem/1475
# 2025-04-16 / 1475. 방 번호 / Silver V

# 기본 접근: 방 번호의 각 숫자의 갯수를 세서, 그 최대값을 출력
# 추가 조건: 6, 9는 묶어서 계산해야 한다.

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

cnt = {k: 0 for k in "0123456789"}
for c in input():
    cnt[c] += 1
cnt_6 = cnt.pop("6")
cnt_9 = cnt.pop("9")
cnt["69"] = (cnt_6 + cnt_9 + 1) // 2
print(max(cnt.values()))
