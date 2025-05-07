# https://www.acmicpc.net/problem/2206
# 2025-05-07 / 2206. 벽 부수고 이동하기 / Gold III

# 1. 최단거리를 구한다
# 2. 부수면 최단거리가 줄어드는 벽을 찾는다
# 이론상 O(n**2) 수준에서 끝나긴 한다.

# 6%에서 실패가 나는것을 확인
# 여러모로 테스트 해봤는데, 벽을 뚫어서 만난 지점이 최단경로가 아닌 경우 문제가 발생
# 아예 애초에 시작점에서 탐색, 끝점에서 탐색을 다른 2차원 배열에서 수행하고, 공통적으로 처리하는게 맞을듯.
# 내일 마저 풀어보는걸로...

import sys

N, M = map(int, input().split())
MAP = sys.stdin.read(N * (M + 1)).splitlines()
A = [[0] * M for _ in range(N)]
B = [[0] * M for _ in range(N)]

def check(arr, y, x):
    # 1. 음수 인덱스 or 인덱스 밖을 찾으면 안됨
    # 2. 벽이 아니여야 함
    # 3. 방문한 적이 없어야 함
    if not (0 <= y < N and 0 <= x < M):
        return False
    if MAP[y][x] == "1":
        return False
    if arr[y][x]:
        return False
    return True

def calc(arr, start):
    current_cells = [start]
    while current_cells:
        next_cells = list()
        for y, x in current_cells:
            checklist = [
                (y-1, x),
                (y, x-1),
                (y+1, x),
                (y, x+1),
            ]
            for y2, x2 in checklist:
                if check(arr, y2, x2):
                    arr[y2][x2] = arr[y][x] + 1
                    next_cells.append((y2, x2))
        current_cells.clear()
        current_cells.extend(next_cells)

# 1. 일단 시작점에서부터 좌표별 최단거리를 구한다. (BFS)
A[0][0] = 1
calc(A, (0, 0))
# for nl in A:
#     print(*nl, sep="\t")
# print("**********************")

# 2. 역방향으로도 동일한 작업 수행
B[N-1][M-1] = 1
calc(B, (N-1, M-1))
# for nl in B:
#     print(*nl, sep="\t")
# print("**********************")

# 3. 벽 부숴보기
# 벽을 기준으로 상하좌우의 A+B의 최소값을 확인
# A,B 들다 한 좌표가 최소인 상황이여도 어차피 1 더하는 것 때문에 결과에 영향을 주진 않음.
results = []
if A[-1][-1]:
    results.append(A[-1][-1])
for y in range(N):
    for x in range(M):
        if A[y][x]:
            continue
        vals_a = [
            A[y2][x2] for y2, x2 in ((y+1, x), (y, x+1), (y-1, x), (y, x-1))
            if 0 <= y2 < N and 0 <= x2 < M and A[y2][x2]
        ]
        vals_b = [
            B[y2][x2] for y2, x2 in ((y+1, x), (y, x+1), (y-1, x), (y, x-1))
            if 0 <= y2 < N and 0 <= x2 < M and B[y2][x2]
        ]
        if vals_a and vals_b:
            results.append(min(vals_a) + min(vals_b) + 1)

print(min(results) if results else -1)
