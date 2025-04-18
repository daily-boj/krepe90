# https://www.acmicpc.net/problem/1166
# 2025-04-18 / 1166. 선물 / Silver III

# 첫번째, N은 반드시 만족해야 한다.
# 두번째, N을 만족하는 가장 큰 p를 찾아야 한다.
# 이분탐색으로 좁혀가며 구현.
# 원래 while (end - start) > 1e-9 로 했는데 시간 초과가 발생.
#  무한 루프를 발생시키는 예외 케이스가 있긴 할텐데 딱히 생각이 나지 않는다.
#  코드 상의 논리적 문제는 없어보이니 아마도 부동소수점 관련 오류가 아닐까?
# 1e+9 / 2**n < 1e-9 가 되는 가장 작은 n이 60이라 60번 반복하는걸로 변경

from functools import reduce

N, L, W, H = map(int, input().split())
area = lambda n: reduce(int.__mul__, [int(x // n) for x in (L, W, H)])

start, end = 0, max(L, W, H)
a = 0
for _ in range(60):
    p = (start + end) / 2
    n = area(p)
    if n >= N:
        a = p
        start = p
    else:
        end = p
print(a)
