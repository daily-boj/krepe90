# https://www.acmicpc.net/problem/33690
# 2025-04-28 / 33690. 포린드롬 / Silver V

# 일단 0.5초 안에 10**9를 전부 도는건 힘들다
# 다른 방법으로 문제에 접근해야 함.
# 문제에서는 P와 floor(P/10)가 펠린드롬이여야 한다고 제시
# 반대로 P/10 쪽에서부터 올라가는 식으로 구하면 되지 않을까?

def is_pal(n):
    s = str(n)
    return s == s[::-1]


prev = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
all_num = []
for _ in range(10):
    new = list()
    for n in prev:
        for i in range(10):
            next_n = n * 10 + i
            if n > 0 and is_pal(next_n):
                new.append(next_n)
    all_num.extend(prev)
    prev.clear()
    prev.extend(new)

N = int(input())
print(sum(1 for n in all_num if n <= N))
