# https://www.acmicpc.net/problem/25955
# 2025-04-24 / 25955. APC는 쉬운 난이도 순일까, 아닐까? / Silver IV

N = int(input())
conv = lambda x: int(f"{'DPGSB'.index(x[0])}{x[1:]:>04}")
arr_in = input().split()
arr_num = list(map(conv, arr_in))
arr_sorted = sorted(arr_num, reverse=True)

# 최대 2개, 항상 큰게 먼저 들어감.
wrong = []
for i in range(N):
    if arr_num[i] != arr_sorted[i]:
        wrong.append(arr_in[i])

if wrong:
    print("KO")
    print(*wrong[::-1])
else:
    print("OK")
