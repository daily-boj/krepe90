# https://www.acmicpc.net/problem/17826
# 2025-01-27 / 17826. 나의 학점은? / Bronze II

# A+: 1~5등
# A0: 6~15등
# B+: 16~30등
# B0: 31~35등
# C+: 36~45등
# C0: 46~48등
# F: 49~50등

S = list(map(int, input().split()))
s = int(input())
i = S.index(s)

if i < 5:
    print("A+")
elif i < 15:
    print("A0")
elif i < 30:
    print("B+")
elif i < 35:
    print("B0")
elif i < 45:
    print("C+")
elif i < 48:
    print("C0")
else:
    print("F")
