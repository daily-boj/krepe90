# https://www.acmicpc.net/problem/15652
# 2025-01-12 / 15652. N과 M (4) / Silver III

# 근데 이걸 DFS라고 불러도 되나?

N, M = map(int, input().split())
results = []


def dfs(a: list, start=1):
    if len(a) == M:
        print(*a)
        return
    for i in range(start, N+1):
        dfs(a + [i], i)


dfs([])
