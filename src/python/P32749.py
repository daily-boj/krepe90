# https://www.acmicpc.net/problem/32749
# 2025-01-12 / 32749. 타노수 / Silver V

# N = 3, T = 2 면 2^(3-2) 자리씩
# 사실 좀 더 최적화할 방법이 있긴 하겠지만 그냥 이정도만...

N, T = map(int, input().split())
X = input()

length = 2 ** (N - T)
result = 0
for i in range(0, 2 ** N, length):
    x = int(X[i: i + length])
    if x > result:
        result = x
print(result)
