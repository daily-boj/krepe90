# https://www.acmicpc.net/problem/32762
# 2025-04-05 / 32762. 더치 페이 / Bronze II

# 인당 평균 지불 금액
# = 인당 지불 금액의 합 / N
# = 전체 음식 금액의 합 / N
# 입퇴장 시간에 속지 말자

import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
rs = 0
[input() for _ in range(N)]
for i in range(M):
    _, p = map(int, input().split())
    rs += p
print(rs / N)
