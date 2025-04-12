# https://www.acmicpc.net/problem/17362
# 2025-04-12 / 17362. 수학은 체육과목 입니다 2 / Bronze IV

# 8개 단위로 엄검중약소약중검 이 반복되기 때문에
# 입력값을 적당히 8로 나눈 값을 엄검중약소약중검의 인덱스에 넣어주는(?) 방식으로 구현.

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

print([1,2,3,4,5,4,3,2][(int(input()) + -1) % 8])
