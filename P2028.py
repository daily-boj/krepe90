# https://www.acmicpc.net/problem/2028
import math
case = int(input())
for i in range(case):
    n = int(input())
    n_len = int(math.log10(n)) + 1
    print("YES" if (n * n) % pow(10, n_len) == n else "NO")
