# https://www.acmicpc.net/problem/8949
# 2025-04-20 / 8949. 대충 더해 / Bronze II

# 숫자로도 충분히 다를수는 있으나 귀찮으니 문자열채로 다룬 다음 더하는걸로
# 풀고나니까 너무 쓰레기같이 푼 것 같다...

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

A, B = input().split()
A = f"{A:>07}"
B = f"{B:>07}"
print(int("".join(map(lambda args: str(int(args[0]) + int(args[1])), zip(A, B)))))
