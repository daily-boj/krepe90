# https://www.acmicpc.net/problem/9655
# 2024-11-11 / 9655. 돌 게임 / Silver V

# 상근(선) / 창영(후)
# -3 or -1
# f(1) = 상근 1
# f(2) = 창영 1 1
# f(3) = 상근 3 / 1 1 1
# f(4) = 창영 3 1 / 1 3 / 1 1 1 1
# f(5) = 상근 3 1 1 / 1 1 3 / 1 1 1 1 1
# ? 그냥 홀짝같은데
print(["CY", "SK"][int(input()) % 2])