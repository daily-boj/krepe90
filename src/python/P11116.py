# https://www.acmicpc.net/problem/11116
# 2025-04-02 / 11116. 교통량 / Silver V

# 검측 지점은 2곳 (왼/오)
# 차량은 양방향에서 올 수 있고, 한 번에 한 대의 차량만
# t에 대해 left[t], left[t+500], right[t+1000], right[t+1500]
#   이 전부 존재하는지만 확인하면 될 것 같은데.

n = int(input())
for _ in range(n):
    m = int(input())
    left = set(map(int, input().split()))
    right = set(map(int, input().split()))

    c = 0
    for t in left:
        if t + 500 in left and t + 1000 in right and t + 1500 in right:
            c += 1
    print(c)
