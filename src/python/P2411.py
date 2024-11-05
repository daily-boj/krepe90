# https://www.acmicpc.net/problem/2411
# 2020-06-10 / 2411. 아이템 먹기 / Gold IV
n, m, a, b = map(int, input().split(maxsplit=3))
items = []
blocks = []
arr = [[(0, 0) for y in range(m + 1)] for x in range(n + 1)]
for i in range(a):
    items.append(tuple(map(int, input().split(maxsplit=1))))
for j in range(b):
    blocks.append(tuple(map(int, input().split(maxsplit=1))))

arr[0][1] = (1, 0)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        self_route, self_item = 0, 0
        if (i, j) in blocks:
            arr[i][j] = (0, 0)
            continue
        if (i, j) in items:
            self_item += 1

        if arr[i - 1][j][1] > arr[i][j - 1][1]:
            # 현재 위치의 아래쪽 원소가 더 많은 별을 지나온 경우
            self_route += arr[i - 1][j][0]
            self_item += arr[i - 1][j][1]
        elif arr[i - 1][j][1] < arr[i][j - 1][1]:
            # 현재 위치의 왼쪽 원소가 더 많은 별을 지나온 경우
            self_route += arr[i][j - 1][0]
            self_item += arr[i][j - 1][1]
        else:
            # 양쪽이 지나온 별의 갯수가 같은경우:
            # 별 값은 그대로, 양쪽 경로값을 더함
            self_route += arr[i - 1][j][0] + arr[i][j - 1][0]
            self_item += arr[i - 1][j][1]
        arr[i][j] = (self_route, self_item) 
print(arr[-1][-1][0])
