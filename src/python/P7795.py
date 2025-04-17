# https://www.acmicpc.net/problem/7795
# 2025-04-17 / 7795. 먹을 것인가 먹힐 것인가 / Silver III

# 두 생명체 A와 B의 크기가 주어졌을 때, A의 크기가 B보다 큰 쌍이 몇 개나 있는지
#  구하는 프로그램을 작성하시오.
# A, B를 일단 정렬
# A를 순회하면서 B 탐색(?)하는 식으로 갯수를 간단히 계산하기.
# pos_b 정의: a보다 작은 가장 큰 b의 idx
# pos_b를 1부터 시작하게 해서 pos_b의 값이 b보다 작은 a의 갯수를 나타내도록도 하였다.
#  반대로 값이 넘어가는걸 방지하기 위한 20001도 끝자락에 또 추가해줬고.
#  다만 이게 좋은 접근방법인지는... 모르겠다.

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = [0] + sorted(map(int, input().split())) + [20001]

    pos_b = 0
    result = 0
    for a in A:
        while pos_b < M and B[pos_b + 1] < a:
            pos_b += 1
        result += pos_b
    print(result)
