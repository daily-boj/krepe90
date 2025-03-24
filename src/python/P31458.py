# https://www.acmicpc.net/problem/31458
# 2025-03-24 / 31458. !!초콜릿 중독 주의!! / Bronze II

# 팩토리얼이 있으면 무조건 숫자는 1
# 즉 s[-1] == 0 이면 우측 계산은 0, 아니면 우측 느낌표 길이와 관계 없이 1
# 왼쪽은... 홀수개면 반전, 짝수면 그대로.

T = int(input())
for _ in range(T):
    s = input()
    n = 0 if s[-1] == "0" else 1
    for i, c in enumerate(s):
        if c in "01":
            print((i % 2) ^ n)
            break
