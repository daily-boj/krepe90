# https://www.acmicpc.net/problem/16435
# 2025-03-11 / 16435. 스네이크버드 / Silver V

# 전부 정렬해놓고 앞에서부터 탐색해도 충분히 문제 없을듯. ( 1 ≤ N ≤ 1000 )
N, L = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

height = L
for fr in h:
    if fr > height:
        break
    else:
        height += 1
print(height)
