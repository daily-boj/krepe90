# https://www.acmicpc.net/problem/32779
# 2025-03-10 / 32779. 가희와 전기 요금 1 / Bronze I

# 설마 부동소수점때문에 틀렸나?

for _ in range(int(input())):
    a, m = map(int, input().split())
    print(int(a * m * 0.00176))
