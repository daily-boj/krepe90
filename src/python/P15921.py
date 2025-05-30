# https://www.acmicpc.net/problem/15921
# 2025-05-30 / 15921. 수찬은 마린보이야!! / Bronze III

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

# 어떤 선수가 대회에서 연습과 비슷하게 꾸준한 기량을 뽐낼 수 있는 확률은 (연습 기록들의 평균값) / (연습 기록들 중 하나를 균일한 확률로 뽑을 때의 기댓값) 이라고 한다
# 첫째 줄에 수찬이의 연습 기록의 개수 N이 주어진다. (0 ≤ N ≤ 100)
# 둘째 줄에 수찬이의 연습 기록 N개가 주어진다. N이 0이면 아무것도 주어지지 않으며 연습 기록은 100 이하의 양의 정수이다.

if input() == "0":
    print("divide by zero")
else:
    A = list(map(int, input().split()))
    n = len(A)
    print(f"{1:.2f}")
