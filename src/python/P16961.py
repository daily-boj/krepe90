# https://www.acmicpc.net/problem/16961
# 2025-04-29 / 16961. 탭 vs 공백 / Bronze I

# 1. 투숙객이 1명 이상인 날의 수
# 2. 가장 많은 투숙객이 있었던 날에 투숙한 사람의 수
# 3. 싸움이 없는 날의 수
# 4. 싸움이 없는 날 중 가장 많은 투숙객이 있었던 날에 투숙한 사람의 수. 싸움이 없는 날이 없으면 0을 출력한다.
# 5. 가장 오랜 기간 투숙한 사람이 투숙한 날의 수

# 1, 2, 3, 4는 1..366 하면서 구하면 될 것 같고
# 주의사항으로, 체크아웃이 18시고 체크인이 09시임.

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

N = int(input())
data = [{"TI": 0, "SI": 0, "TO": 0, "SO": 0} for _ in range(367)]
a1, a2, a3, a4, a5 = 0, 0, 0, 0, 0

for i in range(N):
    # 1. 데이터 전처리
    c, ss, es = input().split()
    s, e = int(ss), int(es)
    # 2. 날짜별 증감량으로 재계산
    data[s][c + "I"] += 1
    data[e][c + "O"] += 1
    # A5. 가장 오랜 기간 투숙한 사람이 투숙한 날의 수
    a5 = max(a5, e - s + 1)

# 3. 날짜순으로 돌면서 계산
t, s = 0, 0
for day in range(1, 367):
    # 아침 9시: 체크인
    t += data[day]["TI"]
    s += data[day]["SI"]
    # A1. 투숙객이 1명 이상인 날의 수
    if t or s:
        a1 += 1
    # A2. 가장 많은 투숙객이 있었던 날에 투숙한 사람의 수
    a2 = max(a2, t + s)
    # A3. 싸움이 없는 날의 수
    if t == s and (t or s):
        a3 += 1
        # A4. 싸움이 없는 날 중 가장 많은 투숙객이 있었던 날에 투숙한 사람의 수. 싸움이 없는 날이 없으면 0을 출력한다.
        a4 = max(a4, t + s)
    # 저녁 6시: 체크아웃
    t -= data[day]["TO"]
    s -= data[day]["SO"]

print(a1, a2, a3, a4, a5, sep="\n")
