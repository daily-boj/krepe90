# https://www.acmicpc.net/problem/11121
# 2025-04-02 / 11121. Communication Channels / Bronze IV

T = int(input())
for _ in range(T):
    i, o = input().split()
    print("OK" if i == o else "ERROR")
