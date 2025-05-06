# https://www.acmicpc.net/problem/2206
# 2025-05-06 / 2206. 벽 부수고 이동하기 / Gold III

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

def check(y, x):
    # 1. 음수 인덱스 or 인덱스 밖을 찾으면 안됨
    # 2. 벽이 아니여야 함
    # 3. 방문한 적이 없어야 함
    if not (0 <= y < N and 0 <= x < M):
        return False
    if MAP[y][x] == "1":
        return False
    if A[y][x]:
        return False
    return True

# 1. 일단 시작점에서부터 좌표별 최단거리를 구한다. (BFS)
A[0][0] = 1
current_cells = [(0, 0)]
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
            if check(y2, x2):
                A[y2][x2] = A[y][x] + 1
                next_cells.append((y2, x2))
    current_cells.clear()
    current_cells.extend(next_cells)
# for nl in A:
#     print(*nl, sep="\t")
# print("**********************")

# 2. 혹시 도착점에 도달하지 못했다면 :: MAP[-1][-1] == -1
#    도착지점에서부터 역으로 동일한 과정 수행
if A[-1][-1] == 0:
    A[-1][-1] = -1
    current_cells = [(N - 1, M - 1)]
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
                if check(y2, x2):
                    A[y2][x2] = A[y][x] - 1
                    next_cells.append((y2, x2))
        current_cells.clear()
        current_cells.extend(next_cells)
    # for nl in A:
    #     print(*nl, sep="\t")
    # print("**********************")

# 3. 벽 부숴보기
# 벽을 기준으로 상하좌우의 A값을 확인
# 양수만 있는 경우 (최소+2)-(최대)
# 양수+음수인 경우 (양수 최소+2)-(음수 최대)
# 음수+음수인 경우는 의미 없으니 건너뛰기
results = [0]
mode_pn = (A[-1][-1] == -1)
for y in range(N):
    for x in range(M):
        if A[y][x]:
            continue
        values = [
            A[y2][x2] for y2, x2 in ((y+1, x), (y, x+1), (y-1, x), (y, x-1))
            if 0 <= y2 < N and 0 <= x2 < M and A[y2][x2]
        ]
        if len(values) < 2:
            continue
        values_p = [n for n in values if n > 0]
        values_n = [n for n in values if n < 0]
        if mode_pn:
            if not values_n or not values_p:
                continue
            mx = max(values_n)
        else:
            if not values_p:
                continue
            mx = max(values_p)
        mn = min(values_p)
        results.append(mn + 2 - mx)

# 결과 출력
if mode_pn:
    print(A[-1][-1] + max(results))
else:
    print(A[-1][-1] + min(results))
