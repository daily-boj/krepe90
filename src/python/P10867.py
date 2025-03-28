# https://www.acmicpc.net/problem/10867
# 2025-03-28 / 10867. 중복 빼고 정렬하기 / Silver V

# 날로 먹는 방법
input()
print(*sorted(set(input().split()), key=int))
