# https://www.acmicpc.net/problem/1439
# 2024-11-15 / 1439. 뒤집기 / Silver V

cnt = {"0": 0, "1": 0}
current = ""
for c in input():
    if c != current:
        cnt[c] += 1
        current = c
print(min(cnt.values()))
