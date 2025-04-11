# https://www.acmicpc.net/problem/5567
# 2025-04-11 / 5567. 결혼식 / Silver II

# 동기임을 저장하는건 dict[int, set] 형태로. key의 동기 집합이 value인 형태. (그 역도 추가)
# set을 사용하기 때문에 중복 처리를 고민하지 않아도 됨

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

N = int(input())
M = int(input())

g: dict[int, set[int]] = {n: set() for n in range(1, N + 1)}
for _ in range(M):
    k, v = map(int, input().split())
    g[k].add(v)
    g[v].add(k)

rs = set(g[1])
rs.update(*(g[i] for i in g[1]))
if 1 in rs:
    rs.remove(1)
print(len(rs))
