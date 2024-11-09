# https://www.acmicpc.net/problem/1932
# 2024-11-09 / 1932. 정수 삼각형 / Silver I

prev_line = [0]
for _ in range(int(input())):
    current_line = [int(n) for n in input().split()]
    sum_left = [a + b for a, b in zip(prev_line + [0], current_line)]
    sum_right = [a + b for a, b in zip([0] + prev_line, current_line)]
    prev_line = [max(left, right) for left, right in zip(sum_left, sum_right)]
print(max(prev_line))
