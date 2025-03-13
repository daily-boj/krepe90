# https://www.acmicpc.net/problem/33541
# 2025-03-14 / 33541. 2025는 무엇이 특별할까? / Bronze III

# for i in range(1000, 10000):
#     a = i // 100
#     b = i % 100
#     if (a + b) ** 2 == i:
#         print(i)

# X = int(input())
# if X < 2025:
#     print(2025)
# elif X < 3025:
#     print(3025)
# elif X < 9801:
#     print(9801)
# else:
#     print(-1)

X = int(input())
for n in (2025, 3025, 9801):
    if X < n:
        print(n)
        break
else:
    print(-1)
