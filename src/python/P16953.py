# https://www.acmicpc.net/problem/16953
# 2025-01-07 / 16953. A → B / Silver II

# 1 -> 1_000_000_000
# a*2 또는 a*10+1
# 1이 10^9가 되려면 2^30은 해줘야 함.
# 탈출 조건만 잘 짜주면 다 탐색 돌려도 될듯?
# 아무 생각 없이 함수 이름 DP로 했는데 DP가 아니잖아 이거

A, B = map(int, input().split())

def dp(n: int) -> int:
    if n == B:
        return 1
    elif n > B:
        return -1
    
    r1 = dp(n * 2)
    r2 = dp(n * 10 + 1)
    if r1 == r2 == -1:
        return -1
    elif r1 > 0:
        return r1 + 1
    elif r2 > 0:
        return r2 + 1
    else:
        return min(r1, r2) + 1

print(dp(A))
