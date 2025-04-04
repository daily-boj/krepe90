# https://www.acmicpc.net/problem/3042
# 2025-04-04 / 3042. 트리플렛 / Silver II

# 세 점의 기울기 구하기
# 그런데 기울기를 진짜로 구해서 비교하면 0으로 나누거나 나눠지는 상황 발생
# 따라서 식을 변형해서 사용

N = int(input())
p = []
for i in range(N):
    s = input()
    for j, c in enumerate(s):
        if c != '.':
            p.append((i, j))
cnt = 0
for i in range(len(p) - 2):
    for j in range(i + 1, len(p) - 1):
        for k in range(j + 1, len(p)):
            p1, p2, p3 = p[i], p[j], p[k]
            if (p1[0] - p2[0]) * (p1[1] - p3[1]) == (p1[0] - p3[0]) * (p1[1] - p2[1]):
                cnt += 1
print(cnt)
