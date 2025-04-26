# https://www.acmicpc.net/problem/12833
# 2025-04-26 / 12833. XORXORXOR / Bronze I

# A^B 를 C번 수행
# B^B=0 이고, A^0=A
# 따라서 C가 홀수면 A^B, C가 짝수면 A를 출력

A, B, C = map(int, input().split())
print(A^B if C & 0x01 else A)
