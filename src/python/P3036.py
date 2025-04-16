# https://www.acmicpc.net/problem/3036
# 2025-04-16 / 3036. 링 / Silver IV

# 입력받은 반지름들을 R이라고 할 때, R[0]/R[n] (1 <= n < N) 을 출력
# 그런데 기약분수 형태로 출력해야 함 -> 최대공약수를 구해 나누어야 함.
# math.gcd 함수가 제공되긴 하는데, 직접 구현도 해보자...

# from math import gcd

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


N = int(input())
R = list(map(int, input().split()))

for r in R[1:]:
    d = gcd(R[0], r)
    print(f"{R[0]//d}/{r//d}")
