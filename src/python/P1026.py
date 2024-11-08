# https://www.acmicpc.net/problem/1026
# 2024-11-08 / 1026. 보물 / Silver IV

# "B에 있는 수는 재배열하면 안된다" <-- 낚이지 말자

N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)
print(sum(a * b for a, b in zip(A, B)))
