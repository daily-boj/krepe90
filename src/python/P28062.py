# https://www.acmicpc.net/problem/28062
# 2025-05-01 / 28062. 준석이의 사탕 사기 / Bronze II

# 합계가 짝수가 되는 가장 큰 부분조합
# 전부 더해서 짝수면 그대로, 홀수라면 가장 작은 홀수를 찾아 빼면 끝

N = int(input())
A = list(map(int, input().split()))
s = sum(A)
if s & 0x01:
    min_odd = 1001
    for a in A:
        if a & 0x01 and a < min_odd:
            min_odd = a
    s -= min_odd
print(s)
