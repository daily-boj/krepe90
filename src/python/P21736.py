# https://www.acmicpc.net/problem/21736
# 2025-03-09 / 21736. 헌내기는 친구가 필요해 / Silver II

# 가장 먼저 생각나는 접근방법
# "방문한 곳" 배열을 따로 만든 다음, I를 시작으로 BFS

N, M = map(int, input().split())
A = [input() for _ in range(N)]

# I의 위치를 찾아서 q에 넣기 (y, x)
q = []
for i, row in enumerate(A):
    if "I" in row:
        q.append((i, row.index("I")))
        break
# 방문 여부 저장, 만난 사람 수도 저장
visited = [[0] * M for _ in range(N)]
meeted = 0
# BFS
while q:
    current = [n for n in q]
    q = []
    for y, x in current:
        visited[y][x] = 1
        if A[y][x] == "P":
            meeted += 1
        # 상하좌우 확인
        if (y - 1) > -1 and not visited[y - 1][x] and A[y - 1][x] != "X":
            q.append((y - 1, x))
            visited[y - 1][x] = 1
        if (y + 1) < N and not visited[y + 1][x] and A[y + 1][x] != "X":
            q.append((y + 1, x))
            visited[y + 1][x] = 1
        if (x - 1) > -1 and not visited[y][x - 1] and A[y][x - 1] != "X":
            q.append((y, x - 1))
            visited[y][x - 1] = 1
        if (x + 1) < M and not visited[y][x + 1] and A[y][x + 1] != "X":
            q.append((y, x + 1))
            visited[y][x + 1] = 1
print(meeted if meeted else "TT")
