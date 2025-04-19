# https://www.acmicpc.net/problem/15886
# 2025-04-19 / 15886. 내 선물을 받아줘 2 / Silver III

# E는 왼쪽으로 한칸, W는 오른쪽으로 한칸.
# 그래프같지만 이번엔 굳이 그래프까지 안가도 되는 문제다.
# 어느 구간 중 일부가 ...WE... 로 되어있다면 방향이 <-/-> 가 돼서 단절(?)되기 때문
# 즉 문자열에서 WE가 몇개인지 세서 +1 한 다음 출력하면 된다.
# 문제 이름 뒤에 '2'가 붙어있으니 진짜 그래프 써서 풀어야 하는 시리즈 문제가 있을듯.

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

input()
print(input().count("WE") + 1)
