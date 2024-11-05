# https://www.acmicpc.net/problem/1504
# 2020-06-14 / 1504. 특정한 최단 경로 / Gold IV
# 나중에 합시다...
from queue import PriorityQueue
from array import array


def dijkstra(graph: list, start: int):
    # distTo, PQ 선언
    PQ = PriorityQueue()
    dist_to = [-1] * n
    edge_to = [None] * n

    # distTo 에 시작점을 초기화
    dist_to[start] = 0
    PQ.put((0, start))
    while not PQ.empty():
        v = PQ.get()
        for w, v_w in graph[v]:     # graph[v]에는 (vertex, weight) 형태의 원소의 인접 list가 있음
            if dist_to[w] > dist_to[v] + v_w:
                dist_to[w] = dist_to[v] + v_w
                edge_to[w] = v_w
                # 여기서부터 마저 소스코드 짜야함.
                if w not in PQ.queue:
                    # PQ에 w가 없으면 해당 값을 삽입
                    # PQ.put((v_w, w), dist_to[w])
                    pass
                else:
                    # 있으면 덮어씌우기. 기존거를 뽑은 다음 다시 삽입하거나, 아니면 값을 갈아치우는 방법이 있을까?
                    # tuple이 아닌 list를 원소로 넣으면 가능할것같기도.
                    pass


# 입력은 1부터 n까지이나 계산의 편의성을 위해 0부터 n-1까지로 하는걸로 결정
n, e = map(int, input().split(maxsplit=1))
graph = [[]] * n
print(graph)
for _ in range(e):
    n1, n2, dist = map(int, input().split())
    n1, n2 = n1 - 1, n2 - 1
    graph[n1].append((n2, dist))
    graph[n2].append((n1, dist))
v1, v2 = map(int, input().split(maxsplit=1))

print(graph)
