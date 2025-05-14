# https://www.acmicpc.net/problem/17945
# 2025-05-14 / 17945. 통학의 신 / Bronze III

# 근의 공식 이용하기
# x ** 0.5 하면 굳이 math.sqrt() 쓸 필요가 없다.

a, b = map(int, input().split())
a *= 2

x1 = int((-a + (a ** 2 - 4 * b) ** .5) / 2)
x2 = int((-a - (a ** 2 - 4 * b) ** .5) / 2)

print(*sorted(set((x1, x2))))
