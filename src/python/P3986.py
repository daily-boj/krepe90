# https://www.acmicpc.net/problem/3986
# 2025-01-12 / 3986. 좋은 단어 / Silver IV

# 대충보면 스택같은 느낌
# A B B' A'
# 글자 쭉 돌면서 마지막거랑 같으면 제거, 다르면 추가

N = int(input())
cnt = 0
for _ in range(N):
    W = input()
    s = [W[0]]
    for c in W[1:]:
        if not s or s[-1] != c:
            s.append(c)
        else:
            s.pop(-1)
    if not s:
        cnt += 1
print(cnt)
