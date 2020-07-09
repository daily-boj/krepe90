# https://www.acmicpc.net/problem/2502
# 2020-07-09 / 2502. 떡 먹는 호랑이 / Silver I
D, K = map(int, input().split())

for i in range(K // 2, K):
    prev1, prev2 = i, K
    cnt = 2
    while True:
        new = prev2 - prev1
        if new > prev1:
            break
        else:
            prev1, prev2 = new, prev1
            cnt += 1
            # print(prev2, end=" ")
        if cnt == D:
            break
    if cnt == D:
        print(f"{prev1}\n{prev2}")
        break
