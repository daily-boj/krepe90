# https://www.acmicpc.net/problem/9455
# 2025-03-30 / 9455. 박스 / Bronze I

# 박스를 아래로 전부 밀어넣기
# 박스 A의 이동거리 -> 박스 아래의 빈칸의 갯수
# 아래 행부터 올라오면서 빈 칸의 갯수를 세기

T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    a = [input().split() for _ in range(m)]

    cnt = 0
    for i in range(n):
        blank = 0
        for j in range(m)[::-1]:
            if a[j][i] == "1":
                cnt += blank
            else:
                blank += 1
    print(cnt)
