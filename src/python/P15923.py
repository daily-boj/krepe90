# https://www.acmicpc.net/problem/15923
# 2025-04-18 / 15923. 욱제는 건축왕이야!! / Bronze III

# 설계도는 욱제가 넘겨주는 좌표 순서대로 i번째 좌표와 i+1번째 좌표를 잇는 선분을 그려 복원할 수 있다
# 선분은 항상 격자에 맞게 주어진다.
# 입력 순서대로 이전 포인트와 다음 포인트의 거리를 구하여 더한다.

p = [tuple(map(int, input().split())) for _ in range(int(input()))]

d = 0
for i, (x1, y1) in enumerate(p):
    x2, y2 = p[i - 1]
    d += abs(x1 - x2) + abs(y1 - y2)
print(d)