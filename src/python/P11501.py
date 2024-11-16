# https://www.acmicpc.net/problem/11501
# 2024-11-16 / 11501. 주식 / Silver II

# 저점일 때 사서 고점에 전부 팔기
# 주가 p[i]를 팔 수 있는 시점: max(p[i:]), 단 p[i]보다 큰 경우.
# max_p 를 정의하여 p[i] 이후 시점의 최대값을 구하기.

for _ in range(int(input())):
    N = int(input())
    p = list(map(int, input().split()))

    max_p = [0] * N
    max_p[N - 1] = p[N - 1]
    for i in range(N - 2, -1, -1):
        max_p[i] = max_p[i + 1] if max_p[i + 1] > p[i] else p[i]

    result = 0
    for i in range(N):
        if p[i] < max_p[i]:
            result += max_p[i] - p[i]
    print(result)
