# https://www.acmicpc.net/problem/7568
# 2025-01-09 / 7568. 덩치 / Silver V

N = int(input())
A: list[tuple[int, int]] = []
for _ in range(N):
    x, y = map(int, input().split())
    A.append((x, y))

print(*[sum(1 for p, q in A if x < p and y < q) + 1 for x, y in A], sep=" ")
