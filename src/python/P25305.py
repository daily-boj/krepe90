# https://www.acmicpc.net/problem/25305
# 2025-03-27 / 25305. 커트라인 / Bronze II

# N, k
# x_1, ...
# 커트라인: 상을 받는 사람들 중 점수가 가장 가장 낮은 사람의 점수
# 내림차순 정렬된 list[int] 타입 x에 대해 k-1번째 (0부터 시작하니)

N, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort(reverse=True)
print(x[k-1])
