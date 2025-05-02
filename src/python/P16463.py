# https://www.acmicpc.net/problem/16463
# 2025-05-02 / 16463. 13일의 금요일 / Silver III

# 13일이 금요일이려면
#                   1
# 2  3  4  5  6  7  8
# 9 10 11 12 13
# 1일이 일요일이여야 함.
# 월...일 -> 0..6

N = int(input())

d1_weekday = 1
cnt = 0
for n in range(2019, N + 1):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if n % 400 == 0:
        days[1] = 29
    elif n % 4 == 0 and n % 100 != 0:
        days[1] = 29

    for d in days:
        if d1_weekday == 6:
            cnt += 1
        d1_weekday = d1_weekday + d
        d1_weekday = d1_weekday % 7
print(cnt)
