# https://www.acmicpc.net/problem/3273
# 2025-01-09 / 3273. 두 수의 합 / Silver III

# "서로 다른" 양의 정수
# 두 수의 합이면 x = n + (x-n)
# 따라서 n과 (x-n)이 있는지만 확인하면 되긴 함.
# n의 범위 -> (x-1) // 2

N = int(input())
A = list(map(int, input().split()))
X = int(input())
A.sort()

left = 0
right = N - 1
result = 0
for n in range(1, (X + 1) // 2):
    while A[left] < n and left < (N - 1):
        left += 1
    while A[right] > (X - n) and right > 0:
        right -= 1
    if A[left] == n and A[right] == (X - n):
        result += 1
print(result)
