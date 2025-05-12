# https://www.acmicpc.net/problem/10103
# 2025-05-12 / 10103. 주사위 게임 / Bronze III

n = int(input())
score_a, score_b = 100, 100
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        continue
    elif a > b:
        score_b -= a
    else:
        score_a -= b
print(score_a, score_b, sep="\n")
