# https://www.acmicpc.net/problem/5397
import sys
import time
st = time.time()
for _ in range(int(input())):
    cur = 0
    res = []
    for c in sys.stdin.readline()[:-1]:
        if c == "<":
            if cur > 0:
                cur = cur - 1
        elif c == "-":
            if cur > 0:
                cur = cur - 1
                res.pop(cur)
        elif c == ">":
            if cur < len(res):
                cur = cur + 1
        else:
            res.insert(cur, c)
            cur += 1
    print("".join(res))
print(time.time() - st)
