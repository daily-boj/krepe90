# https://www.acmicpc.net/problem/15903
# 2024-11-11 / 15903. 카드 합체 놀이 / Silver I

# 문제를 요약하면 '최소값 둘 더해서 덮어씌우기'

# 1. 정렬을 해
# 2. 앞에 두개를 더해
# 3. 다시 정렬을 해
# 4. 앞에 두개를 더해
# 5. 이걸 m번 반복
# 앞부분만 대충 정렬이 되어있으면 되긴 함

import heapq
N, M = map(int, input().split())
A = list(map(int, input().split()))
heapq.heapify(A)

for _ in range(M):
    min_1 = heapq.heappop(A)
    min_2 = heapq.heappop(A)
    heapq.heappush(A, min_1 + min_2)
    heapq.heappush(A, min_1 + min_2)
print(sum(A))
