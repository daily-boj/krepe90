# https://www.acmicpc.net/problem/1894
# 2025-02-03 / 1894. 4번째 점 / Bronze I

# 1. 겹치는 점 찾기
# 2. 계산
    #      4
    # 2 __/
    #     1,3

while True:
    try:
        x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
    except EOFError:
        break

    if (x1, y1) == (x3, y3):
        x = x2 + x4 - x1
        y = y2 + y4 - y1
    elif (x1, y1) == (x4, y4):
        x = x2 + x3 - x1
        y = y2 + y3 - y1
    elif (x2, y2) == (x3, y3):
        x = x1 + x4 - x2
        y = y1 + y4 - y2
    else:
        x = x1 + x3 - x2
        y = y1 + y3 - y2
    print(f"{x:.3f} {y:.3f}")
