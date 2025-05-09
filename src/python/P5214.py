# https://www.acmicpc.net/problem/5214
# 2025-05-09 / 5214. 환승 / Gold II

# 가장 depth가 낮은(?) 경로를 구하는 그래프 탐색 문제
# 메모리 초과로 실패. 생각해보니까 N이 최대 1_000_00 이라서 N ** 2 는 감당이 안된다.

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

N, K, M = map(int, input().split())
can_visit = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    stations = list(map(int, input().split()))
    for i in stations:
        for j in stations:
            can_visit[i][j] = 1
            can_visit[j][i] = 1


visited = [0] * (N + 1)
will_visit = {1}
step = 0
while will_visit:
    this_visit = list(will_visit)
    will_visit.clear()
    step += 1

    for i in this_visit:
        if visited[i]:
            continue
        visited[i] = step
        for j, v in enumerate(can_visit[i]):
            if v and not visited[j]:
                will_visit.add(j)

print(visited[-1])