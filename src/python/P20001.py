# https://www.acmicpc.net/problem/20001
# 2025-05-29 / 20001. 고무오리 디버깅 / Bronze II

cnt = 0
while (c := input()[-1]) != "끝":
    if c == "제":
        cnt += 1
    elif c == "리" and cnt:
        cnt -= 1
    elif c == "리":
        cnt += 2
print("힝구" if cnt else "고무오리야 사랑해")
