# https://www.acmicpc.net/problem/25165
# 2025-05-13 / 25165. 영리한 아리의 포탈 타기 / Bronze II

# 경우의 수만 조심스럽게 생각해서 잘 정리하면 된다.
# 시작방향 (좌/우) + 몹 위치 (시작,끝/중앙) + 동선 겹침 여부


N, M = map(int, input().split())
ac, d = map(int, input().split())
sr, sc = map(int, input().split())

if 1 < sr < N:
    print("NO...")
else:
    if d == 0 and sr == 1 and sc < ac:
        print("NO...")
    elif d == 0 and sr == N and N % 2 == 0:
        print("NO...")
    elif d == 1 and sr == 1 and ac < sc:
        print("NO...")
    elif d == 1 and sr == N and N % 2 == 1:
        print("NO...")
    else:
        print("YES!")
