# https://www.acmicpc.net/problem/31462
# 2025-03-11 / 31462. 삼각 초콜릿 포장 (Sweet) / Silver II

# 위로 뾰족 -> R
# 아래로 뾰족 -> B
# R이 i에 있었음 -> 다음번 i, i+1은 R이여야 함.
# B가 i, i+1에 있었음 -> 다음번 i+1은 B여야 함.
# 문제가 되는 경우: B가 i에는 있는데 i+1에 없는 경우
# R
# RR
# BBR
# RBBR

N = int(input())
checked = [[False] * i for i in range(1, N + 1)]
data = [input() for _ in range(N)]

def check_cell(i, j, c):
    try:
        return data[i][j] == c and not checked[i][j]
    except IndexError:
        return False

def check():
    for i in range(N):
        for j in range(i+1):
            c = data[i][j]
            if checked[i][j]:
                continue
            if c == "R":
                if check_cell(i+1, j, "R") and check_cell(i+1, j+1, "R"):
                    checked[i+1][j] = True
                    checked[i+1][j+1] = True
                else:
                    return 0
            if c == "B":
                if check_cell(i, j+1, "B") and check_cell(i+1, j+1, "B"):
                    checked[i][j+1] = True
                    checked[i+1][j+1] = True
                else:
                    return 0
            checked[i][j] = True
    return 1 if all(map(all, checked)) else 0


print(check())
