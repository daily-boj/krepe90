# https://www.acmicpc.net/problem/2546
# 2020-07-09 / 2546. 경제학과 정원영 / Bronze I
T = int(input())

for t in range(T):
    # 빈 줄 입력
    input()
    N, M = map(int, input().split())
    stu_C = list(map(int, input().split()))
    stu_E = list(map(int, input().split()))
    avg_C = sum(stu_C) / N
    avg_E = sum(stu_E) / M
    print(sum(1 for n in stu_C if n < avg_C and n > avg_E))
