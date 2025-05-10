# https://www.acmicpc.net/problem/5214
# 2025-05-09 / 5214. 환승 / Gold II
# 2025-05-10 / 5214. 환승 / Gold II

# 가장 depth가 낮은(?) 경로를 구하는 그래프 탐색 문제
# 메모리 초과로 실패. 생각해보니까 N이 최대 100_000 이라서 N ** 2 는 감당이 안된다.

# 해시 테이블을 쓰자
# 각 하이퍼튜브가 방문하는 역들을 set 에 저장 (이러면 1000개의 set 존재)
# 역 하나 방문할 때마다 n을 가진 set을 전부 더해서 다음 방문 역으로 계산하기
# -> 역시나 시간초과...
# 병목이 나는 지점을 찾아보자.
# * A. 100000 개에 대해서 BFS 실시
#   * B. 1000 개의 튜브 목록 중 i번 역이 있는 것을 찾기
#   * C. 다음 방문 예정인 역을 추가 (1000개 * 1000번)
# 아무리 해시테이블이 O(1)이여도 이정도면 어렵지...

import sys
input = lambda: sys.stdin.readline().rstrip()

N, K, M = map(int, input().split())
tubes: list[set[int]] = []
for _ in range(M):
    tubes.append(set(map(int, input().split())))

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

        for t in tubes:
            if i not in t:
                continue
            will_visit.update(s for s in t if not visited[s])

print(visited[-1])
